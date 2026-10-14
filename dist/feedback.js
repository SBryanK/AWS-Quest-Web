// Call setEnabled only from a visible preference; pair pulse with visible feedback.
export function createHaptics({navigator:nav=globalThis.navigator,lowMotion=()=>false,now=()=>Date.now()}={}) {
 let enabled=false,last=-Infinity;
 const supported=!!nav&&typeof nav.vibrate==='function';
 const cancel=()=>{if(supported)try{nav.vibrate(0);}catch{}};
 return {supported,setEnabled(value){enabled=!!value;if(!enabled)cancel();},cancel,
  pulse(ms=12){if(!enabled||!supported||lowMotion()||now()-last<90)return false;last=now();try{return nav.vibrate(Math.max(1,Math.min(20,ms)))!==false;}catch{return false;}}
 };
}
