#!/usr/bin/env python3
"""Validate the optional Study Quest JSON contract without changing input files."""
import json,sys
from pathlib import Path

def validate(d):
 errors=[]
 def need(ok,msg):
  if not ok:errors.append(msg)
 def ids(rows,label):
  need(isinstance(rows,list),label+' must be a list')
  if not isinstance(rows,list):return {}
  out={}
  for r in rows:
   if not isinstance(r,dict):errors.append(label+' entry must be an object');continue
   i=r.get('id');need(isinstance(i,str) and bool(i),label+' needs a nonempty string id')
   if not isinstance(i,str):continue
   need(i not in out,'Duplicate '+label+' id '+i);out[i]=r
  return out
 if not isinstance(d,dict):return ['Root must be an object']
 need(d.get('schemaVersion')==1,'Expected schemaVersion 1')
 sources=ids(d.get('sources'),'source');lessons=ids(d.get('lessons'),'lesson')
 pages={}
 for i,s in sources.items():
  n=s.get('pageCount');need(type(n) is int and n>0,i+' needs positive pageCount')
  if type(n) is int and 0<n<=100000:pages[i]=[None]*n
 def span(r,context):
  sid=r.get('source');a=r.get('start');b=r.get('end')
  ok=sid in pages and type(a) is int and type(b) is int and 1<=a<=b<=len(pages[sid])
  need(ok,context+' has invalid source range');return (sid,a,b) if ok else None
 coverage=d.get('coverage',[]);need(isinstance(coverage,list),'coverage must be a list')
 for r in coverage if isinstance(coverage,list) else []:
  if not isinstance(r,dict):errors.append('Coverage row must be an object');continue
  p=span(r,'Coverage');status=r.get('status')
  need(status in ['explained','reference-only','administrative','duplicate','unread','unresolved'],'Invalid coverage status')
  if status=='explained':need(bool(r.get('lessonIds')),'Explained coverage needs lesson links')
  else:need(bool(r.get('note')),'Non-explained coverage needs a reason')
  for lid in r.get('lessonIds',[]):need(lid in lessons,'Coverage links missing lesson '+str(lid))
  if p:
   sid,a,b=p
   for n in range(a-1,b):need(pages[sid][n] is None,f'Overlapping coverage {sid}:{n+1}');pages[sid][n]=status
 for sid,pp in pages.items():
  missing=[str(n+1) for n,s in enumerate(pp) if s is None]
  need(not missing,'Unmapped pages '+sid+': '+','.join(missing[:20]))
 for i,l in lessons.items():
  for key in ['title','mentalModel','example','decision','misconception']:need(isinstance(l.get(key),str) and bool(l[key].strip()),i+' missing '+key)
  need(isinstance(l.get('mechanism'),list) and bool(l.get('mechanism')),i+' needs mechanism steps')
  retrieval=l.get('retrieval',{});need(isinstance(retrieval,dict) and bool(retrieval.get('prompt')) and bool(retrieval.get('answer')),i+' needs retrieval prompt and answer')
  refs=l.get('sources',[]);need(bool(refs),i+' needs source references')
  for r in refs:
   if isinstance(r,dict):span(r,i)
   else:errors.append(i+' invalid source reference')
 for kind in ['concepts','questions']:
  rows=ids(d.get(kind,[]),kind)
  for i,r in rows.items():
   links=r.get('lessonIds',[]);need(isinstance(links,list) and bool(links),i+' needs lessonIds')
   for lid in links:need(lid in lessons,i+' links missing lesson '+str(lid))
   if kind=='concepts':
    for k in ['name','category','cue','chooseWhen','confusion']:need(bool(r.get(k)),i+' missing '+k)
   else:
    opts=r.get('options',[]);correct=r.get('correct',[]);rationales=r.get('rationales',[])
    need(isinstance(opts,list) and len(opts)>=2,i+' needs options')
    valid=isinstance(correct,list) and bool(correct) and all(type(x) is int and 0<=x<len(opts) for x in correct)
    need(valid,i+' invalid correct selections')
    if valid:need(len(correct)==len(set(correct)),i+' duplicate correct selection')
    need(isinstance(rationales,list) and len(rationales)==len(opts) and all(isinstance(x,str) and x.strip() for x in rationales),i+' needs every option rationale')
 return errors
if __name__=='__main__':
 try:
  data=json.loads(Path(sys.argv[1]).read_text());errors=validate(data)
 except (IndexError,OSError,ValueError) as e:
  print('ERROR:',str(e));sys.exit(2)
 if errors:
  print('\n'.join('ERROR: '+s for s in errors));sys.exit(1)
 print('PASS: contract structure, page coverage, lesson/concept links and question choices. Content accuracy and browser behavior still require review.')
