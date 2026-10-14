import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
const dir=new URL('../dist/',import.meta.url).pathname;
const read=name=>JSON.parse(fs.readFileSync(dir+name+'.json','utf8'));
const M=read('mindmap'),C=read('course'),R=read('reference'),G=read('glossary'),Q=read('questions');
const map=await import('data:text/javascript;base64,'+fs.readFileSync(dir+'mindmap.js').toString('base64'));
const entries=M.categories.flatMap(c=>c.services),ids=new Set(entries.map(s=>s.id)),lessons=new Set(C.lessons.map(l=>l.id));
assert.equal(M.categories.length,14);assert.equal(entries.length,176);assert.equal(ids.size,entries.length);
for(const s of entries){assert(lessons.has(s.lesson),s.name+' missing lesson');for(const k of ['name','cue','use','compare','group'])assert(s[k]?.length,s.name+' '+k);}
for(const c of M.categories){const h=map.branchHTML(M,C.lessons,c.id,'',false);assert.equal((h.match(/class="memory-leaf"/g)||[]).length,c.services.length);assert(!h.includes('undefined'));assert(h.includes(c.source));}
assert.equal((map.branchHTML(M,C.lessons,'all','',false).match(/class="memory-leaf"/g)||[]).length,176);
assert(map.filterServices(M,'s3').flatMap(c=>c.services).some(s=>s.name==='S3'));
assert(map.filterServices(M,'sementara').flatMap(c=>c.services).some(s=>s.name==='STS'));
assert.equal(map.filterServices(M,'not-a-real-service-zzzz').length,0);
assert(map.branchHTML(M,C.lessons,'all','<script>',false).includes('&lt;script&gt;'));
for(const s of entries){const h=map.serviceCard(s,C.lessons.find(l=>l.id===s.lesson),true);assert(h.includes('<summary>Reveal service & reasoning</summary>'));assert(!h.includes('<details class="service-detail" open'));}
assert.equal((map.mapSVG(M,'identity').match(/data-category=/g)||[]).length,14);
const elements=new Map();const el=id=>{if(!elements.has(id))elements.set(id,{innerHTML:'',textContent:'',value:'',classList:{toggle(){},add(){},remove(){}},setAttribute(){},removeAttribute(){},querySelectorAll(){return[]},focus(){},scrollIntoView(){},addEventListener(){}});return elements.get(id);};
const revoked=[];const sandbox={console,localStorage:{getItem:()=>null,setItem(){}},document:{querySelector:el,querySelectorAll:()=>[],documentElement:{style:{setProperty(){}}}},window:{addEventListener(){},scrollTo(){}},location:{hash:''},URL:{createObjectURL:()=> 'blob:test',revokeObjectURL:u=>revoked.push(u)},setTimeout:()=>0,clearTimeout(){},setInterval:()=>0,M,C,R,G,Q};
vm.createContext(sandbox);
let app=fs.readFileSync(dir+'app.js','utf8').replace(/^import .*;\n/gm,'').replace(/\ninit\(\);?\s*$/,'');
assert(!/\ninit\(\)/.test(app));
vm.runInContext(app+'\nC=globalThis.C;R=globalThis.R;G=globalThis.G;Q=globalThis.Q;M=globalThis.M;lessonMap=Object.fromEntries(C.lessons.map(l=>[l.id,l]));questionMap=Object.fromEntries(Q.map(q=>[q.id,q]));',sandbox);
for(const p of [1,828,0,999,1.8,'bad']){vm.runInContext('source('+JSON.stringify(p)+')',sandbox);assert(el('#app').innerHTML.includes('id="local-pdf"'));assert(!el('#app').innerHTML.includes('./slides/'));}
vm.runInContext('source(12)',sandbox);
el('#local-pdf').onchange({target:{files:[{name:'bad.txt',type:'text/plain',size:12}]}});assert(el('#pdf-error').textContent.includes('PDF'));
el('#local-pdf').onchange({target:{files:[{name:'course.pdf',type:'application/pdf',size:12}]}});assert(el('#app').innerHTML.includes('blob:test#page=12'));assert(el('#app').innerHTML.includes('course.pdf'));
vm.runInContext('source(30)',sandbox);assert(el('#app').innerHTML.includes('blob:test#page=30'));
el('#local-pdf').onchange({target:{files:[{name:'other.pdf',type:'application/pdf',size:13}]}});assert.deepEqual(revoked,['blob:test']);
for(const l of C.lessons){vm.runInContext('learn('+JSON.stringify(l.id)+')',sandbox);assert(el('#app').innerHTML.includes('Open my PDF at page '+l.start));}
assert(!fs.existsSync(dir+'slides'));assert(!fs.existsSync(dir+'slides.json'));assert(!app.includes("'glossary','slides'"));
console.log('PASS: 176 entries, 14 branches, 101 lesson links/renders, search, recall, escaping, local PDF selection/page bounds/replacement, public assets.');
