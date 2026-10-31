from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import sqlite3, pathlib
DB=pathlib.Path(__file__).with_name('sunday.db')
def db():
 c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; return c
with db() as c:
 c.executescript('CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY,title TEXT,done INTEGER DEFAULT 0); CREATE TABLE IF NOT EXISTS notes(id INTEGER PRIMARY KEY,body TEXT);')
app=FastAPI(title='SUNDAY')
class Task(BaseModel): title:str
class Note(BaseModel): body:str
class Chat(BaseModel): message:str
@app.get('/api/tasks')
def tasks():
 with db() as c:return [dict(r) for r in c.execute('SELECT * FROM tasks ORDER BY id DESC')]
@app.post('/api/tasks')
def add_task(x:Task):
 if not x.title.strip():raise HTTPException(400,'Title required')
 with db() as c:cur=c.execute('INSERT INTO tasks(title) VALUES(?)',(x.title.strip(),));return {'id':cur.lastrowid}
@app.patch('/api/tasks/{i}')
def toggle(i:int):
 with db() as c:
  r=c.execute('SELECT done FROM tasks WHERE id=?',(i,)).fetchone()
  if not r:raise HTTPException(404,'Not found')
  c.execute('UPDATE tasks SET done=? WHERE id=?',(1-r['done'],i))
 return {'ok':True}
@app.delete('/api/tasks/{i}')
def delete(i:int):
 with db() as c:c.execute('DELETE FROM tasks WHERE id=?',(i,))
 return {'ok':True}
@app.get('/api/notes')
def notes():
 with db() as c:return [dict(r) for r in c.execute('SELECT * FROM notes ORDER BY id DESC')]
@app.post('/api/notes')
def note(x:Note):
 with db() as c:cur=c.execute('INSERT INTO notes(body) VALUES(?)',(x.body,));return {'id':cur.lastrowid}
@app.post('/api/chat')
def chat(x:Chat):
 m=x.message.lower()
 reply='Hello! I am SUNDAY in local demo mode.' if any(w in m for w in ['hi','hello','hey']) else 'Use the Tasks and Notes panels to organize your work. Connect a trusted AI provider later for generative answers.'
 return {'reply':reply,'mode':'local-demo'}
app.mount('/',StaticFiles(directory='static',html=True),name='static')
