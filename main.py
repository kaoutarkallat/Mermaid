from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="static")


@app.get("/index", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/checkout", response_class=HTMLResponse)
async def get_checkout(request: Request):
    return templates.TemplateResponse("checkout.html", {"request": request})

@app.get("/legging", response_class=HTMLResponse)
async def get_legging(request: Request):
    return templates.TemplateResponse("legging.html", {"request": request})

@app.get("/shorts", response_class=HTMLResponse)
async def get_shorts(request: Request):
    return templates.TemplateResponse("shorts.html", {"request": request})

@app.get("/shorts2", response_class=HTMLResponse)
async def get_shorts2(request: Request):
    return templates.TemplateResponse("shorts2.html", {"request": request})

@app.get("/shorts3", response_class=HTMLResponse)
async def get_shorts2(request: Request):
    return templates.TemplateResponse("shorts3.html", {"request": request})

@app.get("/bras", response_class=HTMLResponse)
async def get_bras(request: Request):
    return templates.TemplateResponse("bras.html", {"request": request})

@app.get("/bras2", response_class=HTMLResponse)
async def get_bras2(request: Request):
    return templates.TemplateResponse("bras2.html", {"request": request})

@app.get("/bras3", response_class=HTMLResponse)
async def get_bras2(request: Request):
    return templates.TemplateResponse("bras3.html", {"request": request})

@app.get("/legging2", response_class=HTMLResponse)
async def get_legging2(request: Request):
    return templates.TemplateResponse("legging2.html", {"request": request})
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


# @app.get("/index/", response_model=List[schemas.User])
# def get_index(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     return 

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

# pagination
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items