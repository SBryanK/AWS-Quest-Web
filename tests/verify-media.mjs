import assert from 'node:assert/strict';
import fs from 'node:fs';
import {icons,iconHTML,lessonVisuals} from '../dist/service-visuals.mjs';
import {patterns} from '../dist/pattern-data.mjs';
import {stories,diagramSVG} from '../dist/architecture.mjs';
import {relatedMedia,mediaLibrary,videos,initMedia,filterVideos,matchVideos} from '../dist/study-media.mjs';
const root=new URL('../dist/',import.meta.url);
const catalog=JSON.parse(fs.readFileSync(new URL('mindmap.json',root))).categories.flatMap(c=>c.services);
assert.deepEqual(Object.keys(icons).sort(),catalog.map(s=>s.id).sort());
for(const s of catalog){const i=icons[s.id];if(i.src){const svg=fs.readFileSync(new URL(i.src,root),'utf8');assert(svg.includes('<svg'));assert(!/<script\b/i.test(svg));}else assert(iconHTML(s.id).includes('<svg'));}
for(const p of patterns){assert.equal(fs.readFileSync(new URL(p.src,root)).subarray(0,8).toString('hex'),'89504e470d0a1a0a');assert.ok(p.alt.length>35);for(const id of p.services){assert(icons[id]);assert(relatedMedia([id]).includes(p.src));}assert(p.source.startsWith('https://github.com/aws-samples/serverless-patterns/'));}
for(const s of stories){assert.equal(s.nodes.length,s.steps.length);for(const [id] of s.nodes)assert(icons[id],id);for(const [a,b] of s.edges){assert(s.nodes[a]);assert(s.nodes[b]);}for(let i=0;i<s.steps.length;i++){const svg=diagramSVG(s,i);assert.equal((svg.match(/class="story-node active"/g)||[]).length,1);assert(!svg.includes('undefined'));}}
assert(lessonVisuals({id:catalog.find(s=>s.id==='sns').lesson},{categories:[{services:catalog}]}).includes('fanout.png'));
const library=mediaLibrary();assert.equal((library.match(/class="aq-source-figure"/g)||[]).length,12);assert.equal((library.match(/data-play-clip=/g)||[]).length,4);assert(!library.includes('<iframe'));
let click,replaced;globalThis.document={addEventListener(n,f){if(n==='click')click=f;},createElement(tag){return {tag};}};initMedia();for(const v of videos){const btn={dataset:{playClip:v.id},replaceWith(frame){replaced=frame;}};click({target:{closest:()=>btn}});assert.equal(replaced.tag,'iframe');assert.equal(replaced.src,'https://www.youtube-nocookie.com/embed/'+v.id);assert.equal(replaced.title,v.title);}
console.log('PASS: service icon coverage, local diagram binaries, source links, media-to-lesson mappings, six walkthroughs and click-to-load video embeds.');

assert.equal(new Set(videos.map(v=>v.id)).size,videos.length);
for(const v of videos){assert(/^[A-Za-z0-9_-]{11}$/.test(v.id));assert(v.title&&v.cue&&v.publisher&&v.sourceUrl);for(const id of [...v.services,...v.relatedServices])assert(icons[id],id);assert(v.url.includes(v.id));}
const M=JSON.parse(fs.readFileSync(new URL('mindmap.json',root)));
assert(filterVideos(M,{service:'lambda'}).every(v=>[...v.services,...v.relatedServices].includes('lambda')));
assert.equal(filterVideos(M,{query:'never-a-video-zxyz123'}).length,0);
assert(matchVideos(['s3']).length>0);
console.log('PASS: video identities, mappings, search, and selected-service filtering.');
