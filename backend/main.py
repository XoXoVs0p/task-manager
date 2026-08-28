from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uuid
from datetime import datetime

app = FastAPI(title="Task Manager API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Task(BaseModel):
    id: str
    title: str
    description: str = ""
    completed: bool = False
    created_at: str
    updated_at: str

class TaskCreate(BaseModel):
    title: str
    description: str = ""

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

tasks: List[Task] = []

@app.get("/")
def root():
    return {"message": "Task Manager API", "version": "1.0.0"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", response_model=Task)
def create_task(task_data: TaskCreate):
    now = datetime.utcnow().isoformat()
    task = Task(
        id=str(uuid.uuid4()),
        title=task_data.title,
        description=task_data.description,
        completed=False,
        created_at=now,
        updated_at=now,
    )
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, task_data: TaskUpdate):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            if task_data.title is not None:
                tasks[i].title = task_data.title
            if task_data.description is not None:
                tasks[i].description = task_data.description
            if task_data.completed is not None:
                tasks[i].completed = task_data.completed
            tasks[i].updated_at = datetime.utcnow().isoformat()
            return tasks[i]
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(i)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks")
def delete_all_tasks():
    tasks.clear()
    return {"message": "All tasks deleted"}
