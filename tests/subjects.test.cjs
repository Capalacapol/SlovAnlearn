const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict'),path=require('node:path');
const dist=path.resolve(__dirname,'../dist'),storage=new Map();
const c=vm.createContext({console,localStorage:{getItem:k=>storage.get(k)||null,setItem:(k,v)=>storage.set(k,v),removeItem:k=>storage.delete(k)},document:{querySelector:()=>({textContent:'',classList:{add(){},remove(){}}}),visibilityState:'visible'},location:{hash:''},Date,URL,crypto:require('node:crypto').webcrypto,setTimeout:()=>1,clearTimeout(){},confirm:()=>false});
let source=['course.js','diagrams.js','visuals.js','detail-visuals.js','reactivity-visuals.js','maths-data.js','study-tools.js','maths-videos.js'].map(f=>fs.readFileSync(path.join(dist,f),'utf8')).join('\n');
source+='\n'+fs.readFileSync(path.join(dist,'app.js'),'utf8').replace(/init\(\);\s*$/,'');vm.runInContext(source,c);const run=s=>vm.runInContext(s,c);
assert.equal(run('MATHS.lessons.length'),60);assert.equal(run('MATHS.questions.length'),130);assert.equal(run('MATHS.topics.length'),26);
assert.equal(run('MATHS.topics.every(t=>MATHS.lessons.some(l=>l.topic===t.id)&&MATHS.questions.some(q=>q.topic===t.id))'),true);
assert.equal(run('MATHS.lessons.every(l=>l.explanation.length>=3&&l.method.length>=3&&l.worked.steps.length>=3&&CALC_GUIDES[l.tool])'),true);
assert.equal(run('new Set(MATHS.questions.map(q=>q.id)).size'),130);
assert.equal(run('MATHS.questions.filter(q=>q.kind===\'mcq\').every(q=>q.options.length===4&&Number.isInteger(q.correct)&&q.correct>=0&&q.correct<4)'),true);
assert.equal(run('new Set(MATHS.questions.filter(q=>q.kind===\'mcq\').map(q=>q.correct)).size'),4);
run("progress.maths.level='SL'");assert.equal(run('mathLessons().length'),39);assert.equal(run("mathLessons().some(l=>l.hl)"),false);assert.equal(run("mathQuestions().some(q=>q.level==='HL')"),false);
run("progress.maths.level='HL'");assert.equal(run('mathLessons().length'),60);
assert.equal(run("MATHS.lessons.map(l=>{state.id=l.id;let s=mathLesson();return />undefined<|>NaN</.test(s)?l.id:null}).filter(Boolean).length"),0);
assert.equal(run("numericCorrect('3.75',MATH_QUESTION_BY_ID.get('M040N'))"),true);assert.equal(run("numericCorrect('0',MATH_QUESTION_BY_ID.get('M040N'))"),false);assert.equal(run("numericCorrect('',MATH_QUESTION_BY_ID.get('M040N'))"),false);
// A wrong selection turns only the chosen choice red; answer is kept behind reveal.
run("const mq=MATH_QUESTION_BY_ID.get('M001C');progress.maths.results[mq.id]={score:0,choice:(mq.correct+1)%4,at:Date.now()}");
assert.equal(run("mathQuestionCard(MATH_QUESTION_BY_ID.get('M001C')).includes('incorrect')"),true);
assert.equal(run("mathQuestionCard(MATH_QUESTION_BY_ID.get('M001C')).includes('class=\"solution\"')"),false);
run("mathUI.revealed.M001C=true");assert.equal(run("mathQuestionCard(MATH_QUESTION_BY_ID.get('M001C')).includes('class=\"solution\"')"),true);
run("const cq=QUESTIONS.find(q=>q.kind==='mcq');state.chosen[cq.id]=(cq.correct+1)%4;state.revealed[cq.id]=false");assert.equal(run("questionCard(cq).includes('incorrect')"),true);assert.equal(run("questionCard(cq).includes('Reveal correct answer')"),true);
// Maths survives cloud/import validation and local export alongside Chemistry.
run("progress.done['S1.1.1']=true;progress.maths.done['D4.2']=true;progress.maths.results.M040N={score:2,value:'3.75',at:Date.now()}");
assert.equal(run("validatedProgress(JSON.parse(JSON.stringify(progress))).maths.done['D4.2']"),true);assert.equal(run("validatedProgress(JSON.parse(JSON.stringify(progress))).done['S1.1.1']"),true);
assert.equal(run("validatedProgress({done:{'S1.1.1':true}}).maths.level"),'SL');
assert.equal(run("validateMaths({done:{evil:true},results:{evil:{score:99}}}).done.evil"),undefined);
assert.equal(run("meaningfulProgress({maths:{done:{'D4.2':true}}})"),true);
// Timed numeric and MCQ answers are hidden until finish and score automatically.
run("progress.maths.activeTest={id:'math-unit',level:'HL',ids:['M040N','M001C'],answers:{M040N:'3.75',M001C:MATH_QUESTION_BY_ID.get('M001C').correct},deadline:Date.now()+60000};finishMathTest()");
assert.equal(run('progress.maths.activeTest'),null);assert.equal(run('progress.maths.tests[0].scores.M040N'),2);assert.equal(run('progress.maths.tests[0].scores.M001C'),1);
run("state.id='math-unit'");assert.equal(run("mathResult().includes('3 / 3 marks')"),true);
assert.equal(run("subjectHome().includes('Chemistry SL')&&subjectHome().includes('Maths AI HL')"),true);assert.equal(run("subjectHome().includes('Official IB timetable')"),true);
// User-selected dates survive the same cloud validation as lesson progress.
assert.equal(run("validExamDate('2029-02-29')"),false);
assert.equal(run("validExamDate('2028-02-29')"),true);
assert.equal(run("validExamDate('2029-13-10')"),false);
assert.equal(run("validExamDate('<script>')"),false);
assert.equal(run("validatedProgress({examDates:{chemistry:'2029-05-10',maths:'2029-05-12',other:'2029-05-01'}}).examDates.maths"),'2029-05-12');
assert.equal(run("Object.keys(validatedProgress({examDates:{maths:'2029-02-30'}}).examDates).length"),0);
run("progress.maths.level='HL';handleWorkspaceChange({target:{id:'subjectQuickSwitch',value:'maths'}})");
assert.equal(run('location.hash'),'maths');assert.equal(run('progress.maths.level'),'HL');
assert.equal(run("MATHS.lessons.every(l=>MATH_LESSON_VIDEOS[l.id]?.length>0)"),true);
assert.equal(run("Object.values(MATH_LESSON_VIDEOS).flat().every(v=>v.kind==='concept'&&v.focus.length>20&&v.url.startsWith('https://')&&!v.url.includes('product-video-tutorials'))"),true);
assert.equal(run("subjectHome().includes('Slovv <em>an’learn</em>')"),true);
console.log('Workspace controls: valid calendar dates, safe cloud date persistence, quick-switch level preservation and specific concept video coverage passed.');
console.log('Passed: Maths SL/HL filtering, all 60 lesson renders, 130 questions, all 26 subtopics, correct/wrong/reveal logic, numerical marking, dual-subject progress validation, test scoring, subject hub and unpublished-date disclosure.');

assert.equal(run("chemistryHome().includes('class=\"hero\"')"),false);
assert.equal(run("Object.values(MATH_LESSON_VIDEOS).flat().every(v=>v.access==='free')"),true);
