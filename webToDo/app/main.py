from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Optional

from .models import TaskManager
from .storage import save_to_file, load_from_file, delete_file

app = FastAPI(title="FastAPI Task Manager")

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

manager = TaskManager()


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "tasks": manager.tasks
    })


@app.post("/add")
def add_task(title: str = Form(...), description: str = Form(""), status: str = Form("заплановано")):
    manager.add_task(title.strip(), description.strip(), status.strip())
    return RedirectResponse("/", status_code=303)


@app.get("/edit/{index}")
def edit_get(request: Request, index: int):
    task = manager.get_task(index)
    if task is None:
        return RedirectResponse("/", status_code=303)
    return templates.TemplateResponse("edit.html", {
        "request": request,
        "index": index,
        "task": task
    })


@app.post("/edit/{index}")
def edit_post(
    index: int,
    title: Optional[str] = Form(None),
    description: Optional[str] = Form(None),
    status: Optional[str] = Form(None)
):
    if title is not None:
        cleaned_title = title.strip()
    else:
        cleaned_title = None

    if description is not None:
        cleaned_description = description.strip()
    else:
        cleaned_description = None

    if status is not None:
        cleaned_status = status.strip()
    else:
        cleaned_status = None

    manager.edit_task(
        index,
        title=cleaned_title,
        description=cleaned_description,
        status=cleaned_status
    )
    return RedirectResponse("/", status_code=303)


@app.post("/delete/{index}")
def delete(index: int):
    manager.delete_task(index)
    return RedirectResponse("/", status_code=303)


@app.post("/move")
def move(old_index: int = Form(...), new_index: int = Form(...)):
    manager.move_task(old_index, new_index)
    return RedirectResponse("/", status_code=303)


@app.post("/save")
def save(filename: str = Form(...)):
    ok = save_to_file(filename, manager.to_dict_list())
    return RedirectResponse("/", status_code=303)


@app.post("/load")
def load(filename: str = Form(...)):
    data = load_from_file(filename)
    manager.from_dict_list(data)
    return RedirectResponse("/", status_code=303)


@app.post("/delete_file")
def deletefile(filename: str = Form(...)):
    delete_file(filename)
    return RedirectResponse("/", status_code=303)
