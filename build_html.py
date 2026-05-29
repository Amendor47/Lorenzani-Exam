# -*- coding: utf-8 -*-
"""Assemble the single-file index.html from site_data.json + the template."""
import io

with io.open("site_data.json", encoding="utf-8") as f:
    DATA_JSON = f.read()

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Lorenzani Course — Mastery Trainer</title>
<style>
:root{
  --bg:#f7f8fa; --panel:#ffffff; --ink:#1d2330; --muted:#5d6678; --line:#e6e9ef;
  --brand:#1c5fd6; --brand2:#0f47ad; --accent:#0a7e57;
  --def:#1c5fd6; --defbg:#eef3fe; --ex:#0a7e57; --exbg:#e9f6ef;
  --pr:#8a5a00; --prbg:#fdf3e0; --warn:#b22b3b; --warnbg:#fdecee;
  --quote:#5a4bb3; --quotebg:#f0eefb;
  --good:#0a7e57; --bad:#b22b3b; --shadow:0 1px 3px rgba(20,30,60,.08),0 6px 24px rgba(20,30,60,.06);
  --radius:14px;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{background:var(--bg);color:var(--ink);font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}
a{color:var(--brand);text-decoration:none}
button{font-family:inherit}
.app{display:flex;min-height:100vh}
/* Sidebar */
.sidebar{width:300px;flex:0 0 300px;background:var(--panel);border-right:1px solid var(--line);position:sticky;top:0;height:100vh;overflow-y:auto;padding:18px 14px 40px}
.brand{font-weight:800;font-size:18px;letter-spacing:.2px;margin:4px 6px 2px;color:var(--brand2)}
.brand small{display:block;font-weight:600;color:var(--muted);font-size:11.5px;letter-spacing:.3px;margin-top:3px}
.search{width:100%;margin:14px 0 8px;padding:10px 12px;border:1px solid var(--line);border-radius:10px;font-size:14px;background:#fbfcfe}
.navbtns{display:flex;flex-wrap:wrap;gap:6px;margin:6px 4px 12px}
.navbtns button,.resume{flex:1 1 auto;border:1px solid var(--line);background:#fbfcfe;color:var(--ink);border-radius:9px;padding:8px 6px;font-size:12.5px;font-weight:600;cursor:pointer;transition:.15s}
.navbtns button:hover,.resume:hover{background:#eef3fe;border-color:#cfe0ff}
.navbtns button.active{background:var(--brand);color:#fff;border-color:var(--brand)}
.resume{width:100%;margin:0 4px 12px;background:#eaf7f0;border-color:#bfe7d2;color:#0a6b4a}
.modgroup{margin:10px 4px}
.modtitle{font-size:11px;font-weight:800;text-transform:uppercase;letter-spacing:.6px;color:var(--muted);padding:8px 8px 4px}
.seclink{display:flex;align-items:center;gap:8px;padding:7px 9px;border-radius:8px;cursor:pointer;font-size:13.3px;color:var(--ink)}
.seclink:hover{background:#f1f4fb}
.seclink.active{background:#eef3fe;color:var(--brand2);font-weight:700}
.dot{width:9px;height:9px;border-radius:50%;flex:0 0 9px;background:#d6dbe6}
.dot.read{background:#f2c14e}
.dot.mastered{background:var(--good)}
.seclink .pct{margin-left:auto;font-size:11px;color:var(--muted);font-variant-numeric:tabular-nums}
/* Main */
.main{flex:1;min-width:0;padding:26px 34px 80px;max-width:1000px;margin:0 auto;width:100%}
.topbar{display:none}
h1.page{font-size:26px;margin:2px 0 4px;letter-spacing:-.2px}
.sub{color:var(--muted);margin:0 0 22px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:22px 24px;margin:0 0 18px}
.section-head{display:flex;align-items:flex-start;gap:12px;flex-wrap:wrap}
.section-head h2{margin:0;font-size:22px;flex:1 1 auto}
.modtag{display:inline-block;background:#eef3fe;color:var(--brand2);border-radius:999px;padding:3px 11px;font-size:11.5px;font-weight:700;letter-spacing:.2px;margin-bottom:8px}
.block{margin:14px 0;padding:13px 16px;border-radius:10px;border-left:4px solid var(--line);background:#fbfcfe}
.block .lbl{font-size:10.5px;font-weight:800;text-transform:uppercase;letter-spacing:.7px;opacity:.85;margin-bottom:5px;display:block}
.block.def{border-color:var(--def);background:var(--defbg)} .block.def .lbl{color:var(--def)}
.block.ex{border-color:var(--ex);background:var(--exbg)} .block.ex .lbl{color:var(--ex)}
.block.principle{border-color:var(--pr);background:var(--prbg)} .block.principle .lbl{color:var(--pr)}
.block.warn{border-color:var(--warn);background:var(--warnbg)} .block.warn .lbl{color:var(--warn)}
.block.quote{border-color:var(--quote);background:var(--quotebg);font-style:italic} .block.quote .lbl{color:var(--quote)}
.block.text{border-color:#cdd4e2;background:#fff}
.block ul{margin:6px 0 0;padding-left:22px}
.block ul li{margin:4px 0}
.lead{font-weight:700;margin-bottom:4px}
.kw{border-bottom:1.5px dotted var(--brand);cursor:help;font-weight:600}
.btn{display:inline-block;border:none;border-radius:10px;padding:11px 18px;font-size:14.5px;font-weight:700;cursor:pointer;transition:.15s}
.btn.primary{background:var(--brand);color:#fff}
.btn.primary:hover{background:var(--brand2)}
.btn.ghost{background:#fff;border:1px solid var(--line);color:var(--ink)}
.btn.ghost:hover{background:#f1f4fb}
.btn.good{background:var(--good);color:#fff}
.btn.warn{background:#e0a106;color:#fff}
.btn.bad{background:var(--bad);color:#fff}
.row{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.spacer{flex:1}
.muted{color:var(--muted)}
/* Dashboard */
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px;margin-bottom:18px}
.kpi{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);padding:16px 18px;box-shadow:var(--shadow)}
.kpi .n{font-size:30px;font-weight:800;letter-spacing:-.5px}
.kpi .l{color:var(--muted);font-size:12.5px;font-weight:600}
.ring{--p:0;width:120px;height:120px;border-radius:50%;background:conic-gradient(var(--brand) calc(var(--p)*1%),#e9edf5 0);display:flex;align-items:center;justify-content:center;margin:0 auto}
.ring .inner{width:92px;height:92px;border-radius:50%;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center}
.ring .inner b{font-size:26px}
.bar{height:9px;border-radius:6px;background:#e9edf5;overflow:hidden}
.bar>span{display:block;height:100%;background:linear-gradient(90deg,var(--brand),#3f86ff)}
.mod-card{margin-bottom:14px}
.mod-card h3{margin:0 0 4px;font-size:16px}
.dash-sec{display:flex;align-items:center;gap:10px;padding:8px 0;border-top:1px solid var(--line);font-size:14px;cursor:pointer}
.dash-sec:hover{color:var(--brand)}
.dash-sec .pct{margin-left:auto;font-weight:700;font-variant-numeric:tabular-nums}
.badge{font-size:11px;font-weight:700;padding:2px 8px;border-radius:999px}
.badge.ok{background:var(--exbg);color:var(--good)} .badge.mid{background:var(--prbg);color:var(--pr)} .badge.no{background:#eef1f6;color:var(--muted)}
/* Quiz */
.q{margin:16px 0;padding:16px;border:1px solid var(--line);border-radius:12px;background:#fff}
.q .qno{font-size:12px;font-weight:800;color:var(--muted)}
.q .qtext{font-weight:600;margin:6px 0 12px;font-size:15.5px}
.opt{display:block;width:100%;text-align:left;border:1px solid var(--line);background:#fbfcfe;border-radius:9px;padding:11px 14px;margin:7px 0;cursor:pointer;font-size:14.5px;transition:.12s}
.opt:hover{border-color:#bcd0ff;background:#f3f7ff}
.opt.sel{border-color:var(--brand);background:#eaf1ff}
.opt.correct{border-color:var(--good);background:#e9f7f0}
.opt.wrong{border-color:var(--bad);background:#fdeef0}
.fillin{width:100%;padding:11px 13px;border:1px solid var(--line);border-radius:9px;font-size:14.5px}
.feedback{margin-top:11px;padding:11px 13px;border-radius:9px;font-size:14px;display:none}
.feedback.show{display:block}
.feedback.ok{background:#e9f7f0;border:1px solid #bfe7d2}
.feedback.no{background:#fdeef0;border:1px solid #f3c6cd}
.src{margin-top:8px;font-size:13px;color:#444;background:#f6f8fc;border-left:3px solid var(--brand);padding:8px 11px;border-radius:6px}
.pill{display:inline-block;background:#eef3fe;color:var(--brand2);font-size:11px;font-weight:700;border-radius:999px;padding:2px 9px;margin-right:6px}
/* Flashcard */
.flash{perspective:1200px;margin:18px 0}
.flash-inner{position:relative;width:100%;min-height:230px;transition:transform .5s;transform-style:preserve-3d;cursor:pointer}
.flash-inner.flip{transform:rotateY(180deg)}
.face{position:absolute;inset:0;backface-visibility:hidden;border:1px solid var(--line);border-radius:16px;padding:28px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;background:#fff;box-shadow:var(--shadow)}
.face.back{transform:rotateY(180deg);background:#fbfdff}
.face .role{font-size:11px;font-weight:800;letter-spacing:.8px;text-transform:uppercase;color:var(--muted);margin-bottom:12px}
.face .txt{font-size:19px;line-height:1.5}
.face.back .txt{font-size:17px}
.face .hint{position:absolute;bottom:12px;font-size:11.5px;color:var(--muted)}
.tag{position:absolute;top:12px;left:14px;font-size:11px;color:var(--muted)}
/* Exam */
.exam-timer{font-variant-numeric:tabular-nums;font-weight:800;font-size:20px}
.rubric{display:flex;align-items:center;gap:18px;flex-wrap:wrap}
.scorebig{font-size:54px;font-weight:800;letter-spacing:-1px}
.qreview{border-top:1px solid var(--line);padding:12px 0}
.tablewrap{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:14px}
th,td{text-align:left;padding:9px 10px;border-bottom:1px solid var(--line)}
th{font-size:12px;text-transform:uppercase;letter-spacing:.4px;color:var(--muted)}
.hl{background:#fff3bf;border-radius:3px;padding:0 2px}
.searchres{padding:10px 0;border-bottom:1px solid var(--line);cursor:pointer}
.searchres:hover{background:#f6f8fc}
.searchres .t{font-weight:700;color:var(--brand2)}
.empty{color:var(--muted);font-style:italic;padding:20px 0}
.menu-toggle{display:none}
@media(max-width:880px){
  .sidebar{position:fixed;z-index:50;transform:translateX(-100%);transition:.25s;box-shadow:var(--shadow)}
  .sidebar.open{transform:translateX(0)}
  .main{padding:64px 16px 70px}
  .topbar{display:flex;position:fixed;top:0;left:0;right:0;height:52px;background:#fff;border-bottom:1px solid var(--line);align-items:center;gap:12px;padding:0 14px;z-index:40}
  .menu-toggle{display:inline-flex;border:1px solid var(--line);background:#fff;border-radius:8px;padding:7px 11px;font-size:18px;cursor:pointer}
  .topbar .t{font-weight:800;color:var(--brand2)}
  .scrim{display:none;position:fixed;inset:0;background:rgba(10,20,40,.35);z-index:45}
  .scrim.show{display:block}
}
</style>
</head>
<body>
<div class="topbar">
  <button class="menu-toggle" onclick="toggleNav()">☰</button>
  <span class="t">Lorenzani Mastery</span>
</div>
<div class="scrim" id="scrim" onclick="toggleNav()"></div>
<div class="app">
  <aside class="sidebar" id="sidebar">
    <div class="brand">Lorenzani Mastery Trainer<small>Foresight · Industrial Strategy · Digital Policies — the consistent trio</small></div>
    <input class="search" id="globalSearch" placeholder="🔍 Search the full course text…" oninput="onSearch(this.value)"/>
    <button class="resume" onclick="resumeLast()">⏵ Resume where I left off</button>
    <div class="navbtns">
      <button data-view="dashboard" class="active" onclick="go('dashboard')">Dashboard</button>
      <button data-view="flashcards" onclick="go('flashcards')">Flashcards</button>
      <button data-view="exam" onclick="go('exam')">Final Exam</button>
      <button data-view="weak" onclick="go('weak')">Weak Points</button>
      <button data-view="glossary" onclick="go('glossary')">Glossary</button>
    </div>
    <div id="secnav"></div>
  </aside>
  <main class="main" id="main"></main>
</div>
<script>
const DATA = __DATA__;
const KEY = "lorenzani_state_v3";
const MODTITLE = {}; DATA.modules.forEach(m=>MODTITLE[m.id]=m.title);
const SEC = {}; DATA.sections.forEach(s=>SEC[s.id]=s);

/* ---------- state ---------- */
let state = load();
function load(){
  try{ return JSON.parse(localStorage.getItem(KEY)) || fresh(); }
  catch(e){ return fresh(); }
}
function fresh(){
  return { sec:{}, cards:{}, concepts:{}, last:null, exams:[] };
}
function save(){ localStorage.setItem(KEY, JSON.stringify(state)); }
function secState(id){ return state.sec[id] || (state.sec[id]={read:false,best:0,attempts:0}); }
function recordConcept(concept, ok){
  if(!concept) return;
  const c = state.concepts[concept] || (state.concepts[concept]={correct:0,wrong:0});
  if(ok) c.correct++; else c.wrong++;
}

/* ---------- helpers ---------- */
const esc = s => (s==null?"":String(s));
function norm(s){ return (s||"").toLowerCase().replace(/[‘’“”]/g,"'").replace(/[^a-z0-9%]+/g," ").trim(); }
function masteryBadge(best){
  if(best>=80) return '<span class="badge ok">Mastered '+best+'%</span>';
  if(best>0)   return '<span class="badge mid">'+best+'%</span>';
  return '<span class="badge no">Not started</span>';
}

/* ---------- key-term highlighting in reading mode ---------- */
let TERMINDEX = null;
function buildTermIndex(){
  TERMINDEX = DATA.glossary.map(g=>({t:g.term, d:g.def}))
    .sort((a,b)=>b.t.length-a.t.length);
}
function highlightTerms(htmlStr){
  if(!TERMINDEX) buildTermIndex();
  // operate only on text outside existing tags
  return htmlStr.replace(/(<[^>]+>)|([^<]+)/g, (m,tag,text)=>{
    if(tag) return tag;
    let out = text;
    for(const term of TERMINDEX){
      const safe = term.t.replace(/[.*+?^${}()|[\]\\]/g,"\\$&");
      const re = new RegExp("\\b("+safe+")\\b");
      if(re.test(out)){
        out = out.replace(re, '<span class="kw" title="'+term.d.replace(/"/g,"&quot;")+'" onclick="event.stopPropagation();go(\'glossary\',{q:\''+term.t.replace(/'/g,"")+'\'})">$1</span>');
      }
    }
    return out;
  });
}

/* ---------- navigation render ---------- */
function renderNav(){
  const el = document.getElementById("secnav");
  let h="";
  DATA.modules.forEach(m=>{
    const secs = DATA.sections.filter(s=>s.module===m.id);
    if(!secs.length) return;
    h+='<div class="modgroup"><div class="modtitle">'+esc(m.title)+'</div>';
    secs.forEach(s=>{
      const st=secState(s.id);
      const cls = st.best>=80?"mastered":(st.read?"read":"");
      h+='<div class="seclink" data-sec="'+s.id+'" onclick="openSection(\''+s.id+'\')">'+
         '<span class="dot '+cls+'"></span><span>'+esc(s.title)+'</span>'+
         '<span class="pct">'+(st.best?st.best+'%':'')+'</span></div>';
    });
    h+='</div>';
  });
  el.innerHTML=h;
  highlightActiveNav();
}
function highlightActiveNav(){
  document.querySelectorAll(".seclink").forEach(n=>n.classList.toggle("active", n.dataset.sec===current.sec));
  document.querySelectorAll(".navbtns button").forEach(b=>b.classList.toggle("active", b.dataset.view===current.view));
}

/* ---------- routing ---------- */
let current = {view:"dashboard", sec:null};
function go(view, opts){
  current.view=view; current.sec=null;
  if(window.innerWidth<=880) closeNav();
  window.scrollTo(0,0);
  if(view==="dashboard") renderDashboard();
  else if(view==="flashcards") renderFlashcards();
  else if(view==="exam") renderExam();
  else if(view==="weak") renderWeak();
  else if(view==="glossary") renderGlossary(opts&&opts.q);
  highlightActiveNav();
}
function openSection(id){
  current.view="section"; current.sec=id;
  state.last=id; save();
  if(window.innerWidth<=880) closeNav();
  window.scrollTo(0,0);
  renderSection(id);
  highlightActiveNav();
}
function resumeLast(){
  if(state.last && SEC[state.last]) openSection(state.last);
  else go("dashboard");
}

/* ---------- Dashboard ---------- */
function renderDashboard(){
  const secs=DATA.sections;
  const readN=secs.filter(s=>secState(s.id).read).length;
  const masteredN=secs.filter(s=>secState(s.id).best>=80).length;
  const avg=Math.round(secs.reduce((a,s)=>a+secState(s.id).best,0)/secs.length);
  const cardsDue=flashDueCount();
  let h='<h1 class="page">Course Overview Dashboard</h1>'+
    '<p class="sub">Foresight, industrial strategy and digital policies: a new ‘consistent trio’ in the EU — Prof. Dimitri Lorenzani. Master every section below to be ready for a 20/20.</p>';
  h+='<div class="kpis">'+
     '<div class="kpi"><div class="ring" style="--p:'+avg+'"><div class="inner"><b>'+avg+'%</b><span class="l">mastery</span></div></div></div>'+
     '<div class="kpi"><div class="n">'+masteredN+'/'+secs.length+'</div><div class="l">sections mastered (≥80%)</div></div>'+
     '<div class="kpi"><div class="n">'+readN+'/'+secs.length+'</div><div class="l">sections read</div></div>'+
     '<div class="kpi"><div class="n">'+cardsDue+'</div><div class="l">flashcards due now</div></div>'+
     '</div>';
  h+='<div class="row" style="margin-bottom:18px"><button class="btn primary" onclick="startFirstUnread()">▶ Continue studying</button>'+
     '<button class="btn ghost" onclick="go(\'flashcards\')">Review flashcards</button>'+
     '<button class="btn ghost" onclick="go(\'exam\')">Take final exam</button></div>';
  DATA.modules.forEach(m=>{
    const ms=DATA.sections.filter(s=>s.module===m.id); if(!ms.length) return;
    const mavg=Math.round(ms.reduce((a,s)=>a+secState(s.id).best,0)/ms.length);
    h+='<div class="card mod-card"><div class="row"><h3>'+esc(m.title)+'</h3><span class="spacer"></span><b>'+mavg+'%</b></div>'+
       '<div class="bar" style="margin:8px 0 6px"><span style="width:'+mavg+'%"></span></div>';
    ms.forEach(s=>{
      const st=secState(s.id);
      h+='<div class="dash-sec" onclick="openSection(\''+s.id+'\')"><span class="dot '+(st.best>=80?'mastered':(st.read?'read':''))+'"></span>'+
         esc(s.title)+' <span class="pct">'+masteryBadge(st.best)+'</span></div>';
    });
    h+='</div>';
  });
  document.getElementById("main").innerHTML=h;
}
function startFirstUnread(){
  const s=DATA.sections.find(s=>!secState(s.id).read)||DATA.sections[0];
  openSection(s.id);
}

/* ---------- Section (reading + quiz) ---------- */
function renderSection(id){
  const s=SEC[id]; const st=secState(id); st.read=true; save(); renderNav();
  const idx=DATA.sections.findIndex(x=>x.id===id);
  const prev=DATA.sections[idx-1], next=DATA.sections[idx+1];
  let h='<span class="modtag">'+esc(MODTITLE[s.module])+'</span>';
  h+='<div class="card"><div class="section-head"><h2>'+esc(s.title)+'</h2>'+masteryBadge(st.best)+'</div>';
  s.blocks.forEach(b=>{ h+=renderBlock(b); });
  h+='</div>';
  // quiz
  h+='<div class="card" id="quizCard"><div class="row"><h2 style="margin:0;font-size:20px">Comprehension Quiz</h2>'+
     '<span class="spacer"></span><span class="muted">'+s.quiz.length+' questions · from the exact course wording</span></div>'+
     '<p class="muted">Answer all questions, then submit for instant feedback and source passages. Score ≥80% to mark this section mastered.</p>'+
     '<div id="quizBody"></div>'+
     '<div class="row" style="margin-top:14px"><button class="btn primary" onclick="submitQuiz(\''+id+'\')">Submit quiz</button>'+
     '<button class="btn ghost" onclick="renderSectionQuiz(\''+id+'\')">Reset</button></div>'+
     '<div id="quizResult"></div></div>';
  h+='<div class="row">';
  if(prev) h+='<button class="btn ghost" onclick="openSection(\''+prev.id+'\')">← '+esc(prev.title)+'</button>';
  h+='<span class="spacer"></span>';
  if(next) h+='<button class="btn primary" onclick="openSection(\''+next.id+'\')">'+esc(next.title)+' →</button>';
  else h+='<button class="btn good" onclick="go(\'exam\')">Finish · Final Exam →</button>';
  h+='</div>';
  document.getElementById("main").innerHTML=h;
  renderSectionQuiz(id);
}
function renderBlock(b){
  if(b.k==="list"){
    let h='<div class="block text">';
    if(b.lead) h+='<div class="lead">'+highlightTerms(b.lead)+'</div>';
    h+='<ul>';
    b.items.forEach(it=>h+='<li>'+highlightTerms(it)+'</li>');
    h+='</ul></div>'; return h;
  }
  const labels={def:"Definition",ex:"Example",principle:"Key principle",warn:"Exam warning",quote:"Source quote",text:""};
  const lbl=labels[b.k]||"";
  return '<div class="block '+b.k+'">'+(lbl?'<span class="lbl">'+lbl+'</span>':'')+highlightTerms(b.t)+'</div>';
}
function renderSectionQuiz(id){
  const s=SEC[id];
  let h="";
  s.quiz.forEach((q,i)=>{ h+=renderQ(q,i,id); });
  document.getElementById("quizBody").innerHTML=h;
  document.getElementById("quizResult").innerHTML="";
}
function renderQ(q,i,sid){
  let h='<div class="q" id="'+sid+'_q'+i+'"><div class="qno">Question '+(i+1)+' · <span class="pill">'+esc(q.concept)+'</span> '+(q.type==="mcq"?"Multiple choice":"Fill in the blank")+'</div>'+
        '<div class="qtext">'+esc(q.q)+'</div>';
  if(q.type==="mcq"){
    q.options.forEach((o,oi)=>{
      h+='<button class="opt" data-oi="'+oi+'" onclick="pick(\''+sid+'\','+i+','+oi+')">'+esc(o)+'</button>';
    });
  } else {
    h+='<input class="fillin" placeholder="Type your answer…" data-blank="1" onkeydown="if(event.key===\'Enter\')event.preventDefault()"/>';
  }
  h+='<div class="feedback" id="'+sid+'_f'+i+'"></div></div>';
  return h;
}
let picks={};
function pick(sid,i,oi){
  picks[sid+"_"+i]=oi;
  const q=document.getElementById(sid+"_q"+i);
  q.querySelectorAll(".opt").forEach(b=>b.classList.toggle("sel", +b.dataset.oi===oi));
}
function submitQuiz(id){
  const s=SEC[id]; let correct=0;
  s.quiz.forEach((q,i)=>{
    const qEl=document.getElementById(id+"_q"+i);
    const fb=document.getElementById(id+"_f"+i);
    let ok=false, given="";
    if(q.type==="mcq"){
      const sel=picks[id+"_"+i];
      qEl.querySelectorAll(".opt").forEach(b=>{
        const oi=+b.dataset.oi;
        if(oi===q.answer) b.classList.add("correct");
        if(oi===sel && sel!==q.answer) b.classList.add("wrong");
      });
      ok = (sel===q.answer);
      given = (sel!=null)?q.options[sel]:"(no answer)";
    } else {
      const inp=qEl.querySelector("input");
      given=(inp.value||"").trim();
      ok=checkBlank(given, q.accept);
      inp.style.borderColor = ok?"var(--good)":"var(--bad)";
    }
    if(ok) correct++;
    recordConcept(q.concept, ok);
    fb.className="feedback show "+(ok?"ok":"no");
    let exp = ok? "✓ Correct." : "✗ Not quite. Correct answer: <b>"+esc(q.answer)+"</b>.";
    fb.innerHTML = exp + '<div class="src"><b>Source:</b> '+esc(q.source)+'</div>';
  });
  const pct=Math.round(100*correct/s.quiz.length);
  const st=secState(id); st.attempts++; if(pct>st.best) st.best=pct; save(); renderNav();
  const res=document.getElementById("quizResult");
  res.innerHTML='<div class="block '+(pct>=80?'ex':(pct>=50?'principle':'warn'))+'" style="margin-top:16px"><span class="lbl">Result</span>'+
    'You scored <b>'+correct+'/'+s.quiz.length+' ('+pct+'%)</b>. '+
    (pct>=80?'Section mastered! ✅':'Review the highlighted answers and try again to reach 80%.')+
    ' Best so far: <b>'+st.best+'%</b>.</div>';
  res.scrollIntoView({behavior:"smooth",block:"nearest"});
}
function checkBlank(given, accept){
  const g=norm(given); if(!g) return false;
  return accept.some(a=>{ const n=norm(a); return g===n || g.replace(/\s+/g,"")===n.replace(/\s+/g,"") || (n.length>3 && g.includes(n)) || (g.length>3 && n.includes(g)); });
}

/* ---------- Flashcards (spaced repetition) ---------- */
const INTERVALS=[0,1,2,4,7,15,30]; // box -> days
function cardState(i){ return state.cards[i] || (state.cards[i]={box:0,due:0,seen:0,lapses:0}); }
function flashDueCount(){
  const now=Date.now();
  return DATA.flashcards.reduce((n,_,i)=>{ const c=state.cards[i]; return n+((!c||c.due<=now)?1:0); },0);
}
function buildQueue(){
  const now=Date.now();
  let due=[]; DATA.flashcards.forEach((_,i)=>{ const c=state.cards[i]; if(!c||c.due<=now) due.push(i); });
  // prioritize weak-concept cards
  const weak=weakConcepts().map(w=>w.concept);
  due.sort((a,b)=>{
    const wa=weak.indexOf(DATA.flashcards[a].concept), wb=weak.indexOf(DATA.flashcards[b].concept);
    const ra=wa<0?99:wa, rb=wb<0?99:wb;
    if(ra!==rb) return ra-rb;
    return (cardState(a).box)-(cardState(b).box);
  });
  return due;
}
let fq={queue:[],pos:0,flip:false};
function renderFlashcards(){
  fq.queue=buildQueue(); fq.pos=0; fq.flip=false;
  let h='<h1 class="page">Active-Recall Flashcards</h1>'+
    '<p class="sub">Spaced repetition: rate each card. <b>Again</b> re-queues it now, <b>Hard</b> shortens the interval, <b>Easy</b> pushes it further out. Weak-concept cards are shown first.</p>';
  h+='<div class="row" style="margin-bottom:8px"><span class="muted" id="flashCount"></span><span class="spacer"></span>'+
     '<button class="btn ghost" onclick="resetFlash()">Reset all scheduling</button></div>';
  h+='<div id="flashArea"></div>';
  document.getElementById("main").innerHTML=h;
  showCard();
}
function showCard(){
  const area=document.getElementById("flashArea");
  document.getElementById("flashCount").textContent =
    DATA.flashcards.length+" cards total · "+flashDueCount()+" due";
  if(!fq.queue.length){
    area.innerHTML='<div class="card"><div class="block ex"><span class="lbl">All caught up</span>No flashcards are due right now. Great spacing! Come back later, or reset scheduling to drill everything again.</div></div>';
    return;
  }
  if(fq.pos>=fq.queue.length){
    area.innerHTML='<div class="card"><div class="block ex"><span class="lbl">Session complete</span>You reviewed '+fq.queue.length+' cards. '+
      '<div class="row" style="margin-top:12px"><button class="btn primary" onclick="renderFlashcards()">Start another round</button></div></div></div>';
    return;
  }
  const i=fq.queue[fq.pos]; const c=DATA.flashcards[i];
  let h='<div class="card"><div class="muted" style="font-size:13px">Card '+(fq.pos+1)+' of '+fq.queue.length+' · <span class="pill">'+esc(c.concept)+'</span></div>'+
    '<div class="flash"><div class="flash-inner'+(fq.flip?" flip":"")+'" id="flashInner" onclick="flipCard()">'+
      '<div class="face front"><span class="tag">'+esc(c.concept)+'</span><div class="role">Question</div><div class="txt">'+esc(c.front)+'</div><div class="hint">click to reveal</div></div>'+
      '<div class="face back"><span class="tag">'+esc(c.concept)+'</span><div class="role">Answer</div><div class="txt">'+esc(c.back)+'</div><div class="hint">rate your recall below</div></div>'+
    '</div></div>';
  if(fq.flip){
    h+='<div class="row" style="margin-top:10px"><button class="btn bad" onclick="rate(0)">Again</button>'+
       '<button class="btn warn" onclick="rate(1)">Hard</button>'+
       '<button class="btn good" onclick="rate(2)">Easy</button></div>';
  } else {
    h+='<div class="row" style="margin-top:10px"><button class="btn primary" onclick="flipCard()">Show answer</button></div>';
  }
  h+='</div>';
  area.innerHTML=h;
}
function flipCard(){ fq.flip=!fq.flip; showCard(); }
function rate(grade){
  const i=fq.queue[fq.pos]; const c=cardState(i); c.seen++;
  if(grade===0){ c.box=0; c.lapses++; c.due=Date.now(); fq.queue.push(i); }       // Again
  else if(grade===1){ c.box=Math.max(1,c.box); c.due=Date.now()+INTERVALS[Math.min(c.box,INTERVALS.length-1)]*864e5; }
  else { c.box=Math.min(c.box+1,INTERVALS.length-1); c.due=Date.now()+INTERVALS[c.box]*864e5; }
  save(); fq.pos++; fq.flip=false; showCard();
}
function resetFlash(){ if(confirm("Reset spaced-repetition scheduling for all cards?")){ state.cards={}; save(); renderFlashcards(); } }

/* ---------- Weak points ---------- */
function weakConcepts(){
  const arr=Object.keys(state.concepts).map(k=>{
    const c=state.concepts[k]; const total=c.correct+c.wrong;
    return {concept:k, wrong:c.wrong, total, rate: total?c.wrong/total:0};
  }).filter(x=>x.wrong>0);
  arr.sort((a,b)=> b.wrong-a.wrong || b.rate-a.rate);
  return arr.slice(0,10);
}
function renderWeak(){
  const weak=weakConcepts();
  let h='<h1 class="page">Weak Points Tracker</h1>'+
    '<p class="sub">The 10 concepts you miss most often, ranked by number of wrong answers. These are surfaced first in flashcard sessions. Drill them, then re-test.</p>';
  if(!weak.length){
    h+='<div class="card"><div class="empty">No weak points yet — answer some quizzes and the concepts you miss will appear here automatically.</div></div>';
  } else {
    h+='<div class="card"><div class="tablewrap"><table><thead><tr><th>#</th><th>Concept</th><th>Wrong</th><th>Attempts</th><th>Error rate</th><th></th></tr></thead><tbody>';
    weak.forEach((w,i)=>{
      const sec=findSectionForConcept(w.concept);
      h+='<tr><td>'+(i+1)+'</td><td><b>'+esc(w.concept)+'</b></td><td>'+w.wrong+'</td><td>'+w.total+'</td><td>'+Math.round(w.rate*100)+'%</td>'+
         '<td>'+(sec?'<button class="btn ghost" onclick="openSection(\''+sec+'\')">Study</button>':'')+'</td></tr>';
    });
    h+='</tbody></table></div>';
    h+='<div class="row" style="margin-top:14px"><button class="btn primary" onclick="go(\'flashcards\')">Drill these in flashcards</button>'+
       '<button class="btn ghost" onclick="if(confirm(\'Clear weak-point history?\')){state.concepts={};save();renderWeak();}">Clear history</button></div></div>';
  }
  document.getElementById("main").innerHTML=h;
}
function findSectionForConcept(concept){
  const s=DATA.sections.find(s=>s.quiz.some(q=>q.concept===concept) || s.terms.some(t=>t.t===concept));
  return s?s.id:null;
}

/* ---------- Final Exam Simulator ---------- */
let exam=null, examTimerId=null;
function renderExam(){
  if(exam && exam.active){ renderExamRunning(); return; }
  let h='<h1 class="page">Final Exam Simulator</h1>'+
    '<p class="sub">Mimics the real exam: <b>closed-book, timed, randomised</b> questions pulled from <b>all sections</b>. 20 questions, 30 minutes. You are graded out of <b>20</b> with a per-question rubric.</p>';
  const last = state.exams[state.exams.length-1];
  h+='<div class="card"><div class="row"><div><div class="muted">Questions</div><b>20</b></div>'+
     '<div style="margin-left:24px"><div class="muted">Time limit</div><b>30:00</b></div>'+
     '<div style="margin-left:24px"><div class="muted">Pass mark</div><b>16 / 20 (80%)</b></div>'+
     '<span class="spacer"></span><button class="btn primary" onclick="startExam()">▶ Start exam</button></div>';
  if(last){
    h+='<div class="block '+(last.score>=16?'ex':'warn')+'" style="margin-top:14px"><span class="lbl">Last attempt</span>'+
       'Scored <b>'+last.score+'/20</b> ('+last.pct+'%) on '+new Date(last.when).toLocaleString()+'.</div>';
  }
  h+='</div>';
  if(state.exams.length){
    h+='<div class="card"><h3 style="margin-top:0">Attempt history</h3><div class="tablewrap"><table><thead><tr><th>#</th><th>Date</th><th>Score /20</th><th>%</th></tr></thead><tbody>';
    state.exams.slice().reverse().forEach((e,i)=>{ h+='<tr><td>'+(state.exams.length-i)+'</td><td>'+new Date(e.when).toLocaleString()+'</td><td>'+e.score+'</td><td>'+e.pct+'%</td></tr>'; });
    h+='</tbody></table></div></div>';
  }
  document.getElementById("main").innerHTML=h;
}
function allQuestions(){
  const pool=[];
  DATA.sections.forEach(s=>s.quiz.forEach(q=>pool.push(Object.assign({secId:s.id,secTitle:s.title},q))));
  return pool;
}
function shuffle(a){ a=a.slice(); for(let i=a.length-1;i>0;i--){ const j=Math.floor(Math.random()*(i+1)); [a[i],a[j]]=[a[j],a[i]]; } return a; }
function startExam(){
  const pool=shuffle(allQuestions()).slice(0,20);
  exam={active:true, qs:pool, ans:{}, t:1800, started:Date.now()};
  if(examTimerId) clearInterval(examTimerId);
  examTimerId=setInterval(()=>{ exam.t--; const el=document.getElementById("examTimer"); if(el) el.textContent=fmt(exam.t); if(exam.t<=0){ clearInterval(examTimerId); finishExam(); } },1000);
  renderExamRunning();
}
function fmt(s){ s=Math.max(0,s); return String(Math.floor(s/60)).padStart(2,'0')+":"+String(s%60).padStart(2,'0'); }
function renderExamRunning(){
  let h='<div class="card"><div class="row"><h2 style="margin:0">Final Exam — in progress</h2><span class="spacer"></span><span class="exam-timer" id="examTimer">'+fmt(exam.t)+'</span></div>'+
     '<p class="muted">Answer all 20. Closed-book — no peeking. Submit when ready (or the timer will auto-submit).</p></div>';
  exam.qs.forEach((q,i)=>{
    h+='<div class="q"><div class="qno">Q'+(i+1)+' / 20 · <span class="pill">'+esc(q.concept)+'</span></div><div class="qtext">'+esc(q.q)+'</div>';
    if(q.type==="mcq"){
      q.options.forEach((o,oi)=>{ const sel=exam.ans[i]===oi; h+='<button class="opt'+(sel?' sel':'')+'" onclick="examPick('+i+','+oi+')">'+esc(o)+'</button>'; });
    } else {
      h+='<input class="fillin" value="'+esc(exam.ans[i]||"")+'" oninput="exam.ans['+i+']=this.value" placeholder="Type your answer…"/>';
    }
    h+='</div>';
  });
  h+='<div class="row"><button class="btn primary" onclick="finishExam()">Submit exam for grading</button>'+
     '<button class="btn ghost" onclick="if(confirm(\'Abandon this exam?\')){exam.active=false;clearInterval(examTimerId);renderExam();}">Abandon</button></div>';
  document.getElementById("main").innerHTML=h;
}
function examPick(i,oi){ exam.ans[i]=oi; renderExamRunning(); }
function finishExam(){
  clearInterval(examTimerId); exam.active=false;
  let correct=0; const review=[];
  exam.qs.forEach((q,i)=>{
    let ok=false, given;
    if(q.type==="mcq"){ given=(exam.ans[i]!=null)?q.options[exam.ans[i]]:"(no answer)"; ok=(exam.ans[i]===q.answer); }
    else { given=(exam.ans[i]||"").trim()||"(no answer)"; ok=checkBlank(given,q.accept); }
    if(ok) correct++; recordConcept(q.concept, ok);
    review.push({q,given,ok});
  });
  const score=Math.round(20*correct/exam.qs.length);
  const pct=Math.round(100*correct/exam.qs.length);
  state.exams.push({when:Date.now(),score,pct,correct,total:exam.qs.length}); save(); renderNav();
  let grade = pct>=90?"Distinction":pct>=80?"Pass with merit":pct>=60?"Borderline":"Fail — keep studying";
  let h='<h1 class="page">Exam Results & 20/20 Rubric</h1>';
  h+='<div class="card"><div class="rubric"><div class="scorebig">'+score+'<span style="font-size:24px;color:var(--muted)">/20</span></div>'+
     '<div><div class="bar" style="width:240px"><span style="width:'+pct+'%"></span></div>'+
     '<div class="muted" style="margin-top:6px">'+correct+' of '+exam.qs.length+' correct · '+pct+'% · <b>'+grade+'</b></div></div>'+
     '<span class="spacer"></span><button class="btn primary" onclick="startExam()">Retake</button>'+
     '<button class="btn ghost" onclick="renderExam()">Done</button></div>';
  h+='<div class="block '+(score>=16?'ex':'warn')+'" style="margin-top:14px"><span class="lbl">Verdict</span>'+
     (score>=16?'You are exam-ready on this sample. Repeat with fresh randomised sets until 20/20 is consistent.':'Below the 16/20 target. Review the missed questions below — each links to its source — and revisit those sections.')+'</div></div>';
  h+='<div class="card"><h3 style="margin-top:0">Per-question review</h3>';
  review.forEach((r,i)=>{
    h+='<div class="qreview"><div class="row"><b>Q'+(i+1)+'.</b> <span class="pill">'+esc(r.q.concept)+'</span> '+
       (r.ok?'<span class="badge ok">Correct</span>':'<span class="badge no" style="background:var(--warnbg);color:var(--bad)">Incorrect</span>')+'</div>'+
       '<div style="margin:6px 0">'+esc(r.q.q)+'</div>'+
       '<div class="muted">Your answer: '+esc(r.given)+'</div>'+
       (r.ok?'':'<div>Correct answer: <b>'+esc(r.q.answer)+'</b></div>')+
       '<div class="src"><b>Source:</b> '+esc(r.q.source)+' <a href="#" onclick="openSection(\''+r.q.secId+'\');return false;">↗ '+esc(r.q.secTitle)+'</a></div></div>';
  });
  h+='</div>';
  document.getElementById("main").innerHTML=h; window.scrollTo(0,0);
}

/* ---------- Glossary ---------- */
function renderGlossary(query){
  let h='<h1 class="page">Word-by-Word Glossary</h1>'+
    '<p class="sub">'+DATA.glossary.length+' technical terms and proper nouns extracted from the course. Each links back to its source section.</p>'+
    '<input class="search" id="gloSearch" placeholder="Filter terms…" value="'+esc(query||"")+'" oninput="filterGlo(this.value)" style="max-width:420px"/>'+
    '<div id="gloList"></div>';
  document.getElementById("main").innerHTML=h;
  filterGlo(query||"");
  if(query){ const i=document.getElementById("gloSearch"); i.focus(); }
}
function filterGlo(q){
  const n=norm(q);
  const list=DATA.glossary.filter(g=> !n || norm(g.term).includes(n) || norm(g.def).includes(n));
  let h='<div class="card">';
  if(!list.length) h+='<div class="empty">No matching terms.</div>';
  list.forEach(g=>{
    h+='<div class="qreview"><div class="row"><b>'+esc(g.term)+'</b>'+
       (g.sec?'<span class="spacer"></span><button class="btn ghost" onclick="openSection(\''+g.sec+'\')">↗ Source</button>':'')+'</div>'+
       '<div style="margin-top:4px">'+esc(g.def)+'</div>'+
       (g.secTitle?'<div class="muted" style="font-size:12.5px;margin-top:4px">in: '+esc(g.secTitle)+'</div>':'')+'</div>';
  });
  h+='</div>';
  document.getElementById("gloList").innerHTML=h;
}

/* ---------- Global search ---------- */
function onSearch(q){
  if(!q || q.trim().length<2){ if(current.view==="search") go("dashboard"); return; }
  current.view="search";
  const n=norm(q);
  const results=[];
  DATA.sections.forEach(s=>{
    let hay=s.title+" ";
    s.blocks.forEach(b=>{ hay += (b.t||"")+" "+(b.lead||"")+" "+((b.items||[]).join(" "))+" "; });
    s.terms.forEach(t=>hay+=t.t+" "+t.d+" ");
    if(norm(hay).includes(n)){
      // find a snippet
      const plain=hay.replace(/<[^>]+>/g," ");
      const li=plain.toLowerCase().indexOf(q.toLowerCase());
      let snip = li>=0? plain.slice(Math.max(0,li-50), li+90) : plain.slice(0,140);
      results.push({id:s.id,title:s.title,mod:MODTITLE[s.module],snip});
    }
  });
  let h='<h1 class="page">Search</h1><p class="sub">'+results.length+' section'+(results.length===1?'':'s')+' match “'+esc(q)+'”.</p><div class="card">';
  if(!results.length) h+='<div class="empty">No matches in the course text.</div>';
  results.forEach(r=>{
    const re=new RegExp("("+q.replace(/[.*+?^${}()|[\]\\]/g,"\\$&")+")","ig");
    h+='<div class="searchres" onclick="openSection(\''+r.id+'\')"><div class="t">'+esc(r.title)+'</div>'+
       '<div class="muted" style="font-size:12px">'+esc(r.mod)+'</div>'+
       '<div style="font-size:13.5px;color:#444">…'+esc(r.snip).replace(re,'<span class="hl">$1</span>')+'…</div></div>';
  });
  h+='</div>';
  document.getElementById("main").innerHTML=h;
  highlightActiveNav();
}

/* ---------- nav toggle (mobile) ---------- */
function toggleNav(){ const s=document.getElementById("sidebar"); s.classList.toggle("open"); document.getElementById("scrim").classList.toggle("show", s.classList.contains("open")); }
function closeNav(){ document.getElementById("sidebar").classList.remove("open"); document.getElementById("scrim").classList.remove("show"); }

/* ---------- init ---------- */
buildTermIndex();
renderNav();
renderDashboard();
</script>
</body>
</html>"""

out = HTML.replace("__DATA__", DATA_JSON)
with io.open("index.html", "w", encoding="utf-8") as f:
    f.write(out)
print("wrote index.html", len(out), "bytes")
