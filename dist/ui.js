import {createHaptics} from './feedback.js';
const PREF_KEY='architect-quest-display-v1';
const defaults={focus:false,lowMotion:false,haptics:false};
let prefs={...defaults},initialized=false;
try{const p=JSON.parse(localStorage.getItem(PREF_KEY)||'{}');for(const k of Object.keys(defaults))if(typeof p[k]==='boolean')prefs[k]=p[k];}catch{}
const media=globalThis.matchMedia?.('(prefers-reduced-motion: reduce)');
const staticMode=new URLSearchParams(location.search).get('static')==='1';
const lowMotion=()=>staticMode||!!media?.matches||prefs.lowMotion;
const feedback=createHaptics({lowMotion});
function persist(){try{localStorage.setItem(PREF_KEY,JSON.stringify(prefs));}catch{const e=document.querySelector('#preference-status');if(e)e.textContent='Applied for this visit; browser storage is unavailable.';}}
function apply(){
 document.documentElement.dataset.lowMotion=String(lowMotion());
 document.body.classList.toggle('focus-mode',prefs.focus);
 const focus=document.querySelector('#focus-toggle');if(focus){focus.setAttribute('aria-pressed',String(prefs.focus));focus.setAttribute('aria-label',prefs.focus?'Exit focus mode':'Enter focus mode');focus.querySelector('span').textContent=prefs.focus?'Exit focus':'Focus';}
 const low=document.querySelector('#low-motion');if(low){low.checked=lowMotion();low.disabled=staticMode||!!media?.matches;}
 const h=document.querySelector('#haptics');if(h){h.checked=prefs.haptics;h.disabled=!feedback.supported;}
 const note=document.querySelector('#haptics-note');if(note)note.textContent=!feedback.supported?'Vibration is unavailable in this browser. Visual feedback stays on.':lowMotion()?'Vibration pauses while reduced motion is active.':'Optional short taps on supported devices; hardware may ignore them.';
 const m=document.querySelector('#motion-note');if(m)m.textContent=staticMode?'Static URL mode is active.':media?.matches?'Your device requests reduced motion.':'Keep transitions still while reading.';
 feedback.setEnabled(prefs.haptics);
}
function closeNav(returnFocus=false){const b=document.querySelector('#nav-toggle');document.body.classList.remove('nav-open');b?.setAttribute('aria-expanded','false');if(returnFocus)b?.focus();}
export function syncUI({focus=false}={}){
 const tab=location.hash.replace(/^#/,'').split('/')[0]||'home';document.body.dataset.view=tab;
 closeNav();apply();
 if(focus)document.querySelector('#main')?.focus({preventScroll:true});
}
export function initUI(){
 if(initialized)return;initialized=true;
 document.querySelector('#nav-toggle')?.addEventListener('click',()=>{const open=document.body.classList.toggle('nav-open');document.querySelector('#nav-toggle').setAttribute('aria-expanded',String(open));});
 document.querySelector('#focus-toggle')?.addEventListener('click',()=>{prefs.focus=!prefs.focus;apply();persist();});
 document.querySelector('#low-motion')?.addEventListener('change',e=>{prefs.lowMotion=e.target.checked;apply();persist();});
 document.querySelector('#haptics')?.addEventListener('change',e=>{prefs.haptics=e.target.checked;apply();persist();if(prefs.haptics)feedback.pulse();});
 document.addEventListener('click',e=>{
  const c=e.target.closest('button,a[href],summary');
  if(c&&!c.disabled&&c.getAttribute('aria-disabled')!=='true'&&!c.closest('#preferences'))feedback.pulse();
  const browser=e.target.closest('.lesson-nav-toggle');if(browser){const open=browser.getAttribute('aria-expanded')!=='true';browser.setAttribute('aria-expanded',String(open));browser.closest('.sidebar').classList.toggle('lesson-nav-open',open);}
  const p=document.querySelector('#preferences');if(p?.open&&!p.contains(e.target))p.open=false;
  if(!e.target.closest('#study-nav,#nav-toggle'))closeNav();
 },{capture:true});
 document.addEventListener('keydown',e=>{if(e.key==='Escape'){const p=document.querySelector('#preferences');if(p?.open){p.open=false;p.querySelector('summary').focus();}if(document.body.classList.contains('nav-open'))closeNav(true);}});
 document.addEventListener('visibilitychange',()=>{if(document.hidden)feedback.cancel();});
 media?.addEventListener?.('change',apply);apply();
}
