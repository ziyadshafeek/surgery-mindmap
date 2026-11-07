# Assemble all 10 Surgery mindmap chunks into one JSON + a single-file
# interactive HTML viewer (collapsible tree + search). No CDN, works offline.
import json, glob, os

OUTDIR = "/home/hatch/workspace/mindmap/surgery"
topics = []
for f in sorted(glob.glob(os.path.join(OUTDIR, "chunk-*.json"))):
    topics.extend(json.load(open(f, encoding="utf-8")))
assert [t["id"] for t in topics] == [f"surgery-t{i:02d}" for i in range(1, 43)], "topic order/ids wrong"

def count(n):
    return 1 + sum(count(c) for c in n.get("children", []))
total_nodes = sum(count(t) for t in topics)

with open(os.path.join(OUTDIR, "surgery-mindmap.json"), "w", encoding="utf-8") as f:
    json.dump({"subject": "Surgery", "exam": "Second Sessional, Mon 09/11/2026",
               "topics": len(topics), "nodes": total_nodes, "data": topics},
              f, ensure_ascii=False, indent=1)

data_json = json.dumps(topics, ensure_ascii=False).replace("</", "<\\/")

html = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Surgery Mindmap — Second Sessional</title>
<style>
body{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;margin:0;background:#fff;color:#111;line-height:1.45}
header{position:sticky;top:0;background:#fff;border-bottom:2px solid #111;padding:10px 14px;z-index:5}
h1{font-size:18px;margin:0 0 2px} .sub{font-size:13px;color:#444;margin:0}
#search{width:100%;box-sizing:border-box;font-size:16px;padding:10px;margin-top:8px;border:2px solid #111;border-radius:8px}
#meta{font-size:13px;color:#444;margin-top:6px}
.btns{display:flex;gap:8px;margin-top:8px;flex-wrap:wrap}
button{font-size:14px;padding:8px 12px;border:2px solid #111;border-radius:8px;background:#fff;cursor:pointer}
button:active{background:#eee}
#topics{padding:6px 14px 40px;max-width:900px}
.topic{border:2px solid #111;border-radius:10px;margin:14px 0;padding:10px 12px}
.topic>h2{font-size:16px;margin:0;cursor:pointer}
.topic>h2 .n{color:#666;font-weight:400;font-size:13px}
ul{list-style:none;margin:6px 0 0;padding-left:18px}
li{margin:4px 0}
.node{cursor:pointer}
.node>.t{border-radius:6px;padding:2px 4px}
.node>.t:hover{background:#f0f0f0}
.caret{display:inline-block;width:18px;color:#666;font-weight:700}
.leaf .caret{visibility:hidden}
.detail{display:block;color:#333;font-size:14px;margin:2px 0 2px 22px}
mark{background:#ffe45e}
.hidden{display:none}
.match-note{font-size:13px;color:#444}
</style></head><body>
<header>
<h1>Surgery Mindmap — Second Sessional</h1>
<p class="sub">Exam Mon 09/11/2026 &middot; replaces the full notes &middot; every point from the source notes, nothing invented</p>
<input id="search" type="search" placeholder="Search all 42 topics — e.g. phaeochromocytoma, BI-RADS, Wells…">
<div id="meta"></div>
<div class="btns">
<button id="expandAll">Expand all</button>
<button id="collapseAll">Collapse all</button>
<button id="showTopics">Topic list</button>
</div>
</header>
<div id="topics"></div>
<script>
const DATA = __DATA__;
const root = document.getElementById('topics');
const meta = document.getElementById('meta');
let totalNodes = 0;
function countNodes(n){ let c=1; (n.children||[]).forEach(ch=>c+=countNodes(ch)); return c; }
DATA.forEach(t=> totalNodes += countNodes(t));
meta.textContent = DATA.length + ' topics · ' + totalNodes.toLocaleString() + ' nodes · tap any heading to open/close it.';
function el(tag, cls, text){ const e=document.createElement(tag); if(cls) e.className=cls; if(text!=null) e.textContent=text; return e; }
function buildNode(n){
  const li = el('li', 'node' + ((n.children&&n.children.length)?'':' leaf'));
  const t = el('span','t'); const caret = el('span','caret', (n.children&&n.children.length)?'▸':'•');
  t.appendChild(caret); t.appendChild(document.createTextNode(n.title));
  li.appendChild(t);
  if(n.detail){ li.appendChild(el('span','detail', n.detail)); }
  if(n.children&&n.children.length){
    const ul = el('ul'); ul.classList.add('hidden');
    n.children.forEach(ch=> ul.appendChild(buildNode(ch)));
    li.appendChild(ul);
    t.addEventListener('click', ()=>{ ul.classList.toggle('hidden'); caret.textContent = ul.classList.contains('hidden')?'▸':'▾'; });
  }
  return li;
}
function render(){
  root.innerHTML='';
  DATA.forEach(t=>{
    const box = el('section','topic'); box.id = t.id;
    const h = el('h2', null, t.title + ' ');
    h.appendChild(el('span','n','· '+countNodes(t)+' nodes'));
    const ul = el('ul');
    (t.children||[]).forEach(ch=> ul.appendChild(buildNode(ch)));
    h.addEventListener('click', ()=>{ ul.classList.toggle('hidden'); });
    box.appendChild(h); box.appendChild(ul); root.appendChild(box);
  });
}
render();
document.getElementById('expandAll').addEventListener('click', ()=>{
  document.querySelectorAll('#topics ul').forEach(u=>u.classList.remove('hidden'));
  document.querySelectorAll('.caret').forEach(c=>{ if(c.textContent==='▸') c.textContent='▾'; });
});
document.getElementById('collapseAll').addEventListener('click', ()=>{
  document.querySelectorAll('#topics .topic > ul, #topics li > ul').forEach(u=>u.classList.add('hidden'));
  document.querySelectorAll('.caret').forEach(c=>{ if(c.textContent==='▾') c.textContent='▸'; });
});
document.getElementById('showTopics').addEventListener('click', ()=>{
  document.getElementById('search').value='';
  document.querySelectorAll('.topic').forEach(b=>b.classList.remove('hidden'));
  document.querySelectorAll('#topics li').forEach(li=>li.classList.remove('hidden'));
  document.querySelectorAll('mark').forEach(m=>{ const p=m.parentNode; p.replaceChild(document.createTextNode(m.textContent), m); p.normalize(); });
  window.scrollTo({top:0, behavior:'smooth'});
});
const search = document.getElementById('search');
search.addEventListener('input', ()=>{
  const q = search.value.trim().toLowerCase();
  document.querySelectorAll('mark').forEach(m=>{ const p=m.parentNode; p.replaceChild(document.createTextNode(m.textContent), m); p.normalize(); });
  if(!q){ document.querySelectorAll('.topic').forEach(b=>b.classList.remove('hidden')); document.querySelectorAll('#topics li').forEach(li=>li.classList.remove('hidden')); meta.textContent = DATA.length + ' topics · ' + totalNodes.toLocaleString() + ' nodes · tap any heading to open/close it.'; return; }
  let hits = 0;
  document.querySelectorAll('.topic').forEach(box=>{
    let boxHits = 0;
    box.querySelectorAll('li').forEach(li=>{
      const text = li.textContent.toLowerCase();
      const hit = text.includes(q);
      li.classList.toggle('hidden', !hit);
      if(hit){
        boxHits++;
        let p = li.parentElement;
        while(p && p!==box){ if(p.tagName==='UL') p.classList.remove('hidden'); const par=p.parentElement; p = par && par.tagName==='LI' ? par.parentElement : null; }
        li.querySelectorAll(':scope > .t, :scope > .detail').forEach(span=>{
          const idx = span.textContent.toLowerCase().indexOf(q);
          if(idx>=0){ const mark=document.createElement('mark'); const node=span.childNodes[span.childNodes.length-1]; const txt=node.textContent; node.textContent=txt.slice(0,idx); mark.textContent=txt.slice(idx,idx+q.length); span.insertBefore(mark, span.childNodes[span.childNodes.length]); span.appendChild(document.createTextNode(txt.slice(idx+q.length))); }
        });
      }
    });
    const h = box.querySelector('h2');
    const hHit = h.textContent.toLowerCase().includes(q);
    box.classList.toggle('hidden', !(boxHits||hHit));
    if(hHit && !boxHits){ box.querySelectorAll('li').forEach(li=>li.classList.remove('hidden')); }
    hits += boxHits;
  });
  meta.textContent = hits + ' matching point' + (hits===1?'':'s') + ' for “' + search.value.trim() + '” — tap a result to open its branch.';
});
</script></body></html>
"""
html = html.replace("__DATA__", data_json)
with open(os.path.join(OUTDIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("topics:", len(topics), "nodes:", total_nodes)
print("html bytes:", len(html.encode("utf-8")))
print("wrote surgery-mindmap.json and index.html")
