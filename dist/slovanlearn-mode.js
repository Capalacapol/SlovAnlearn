/* Display settings are local to this browser; account and calculator settings remain in the app. */
(function(){'use strict';const key='slovanlearn-display-mode',root=document.documentElement,selector=document.getElementById('settingsTheme'),meta=document.querySelector('meta[name="theme-color"]');
function get(){try{return localStorage.getItem(key)==='dark'?'dark':'light'}catch{return root.getAttribute('data-atlas-theme')==='dark'?'dark':'light'}}
function set(mode,persist=true){const dark=mode==='dark';if(dark)root.setAttribute('data-atlas-theme','dark');else root.removeAttribute('data-atlas-theme');if(meta)meta.setAttribute('content',dark?'#101b2d':'#f5f7fc');if(selector)selector.value=dark?'dark':'light';if(persist)try{localStorage.setItem(key,dark?'dark':'light')}catch{}}
window.SlovAnLearnTheme=Object.freeze({get,set});set(get(),false);if(selector)selector.addEventListener('change',()=>set(selector.value));window.addEventListener('storage',e=>{if(e.key===key||e.key===null)set(get(),false)});
})();
