from fastapi import FastAPI

from routers import company, job
from database import engine, Base
from models import company as company_model
from models import job as job_model

app = FastAPI()

print(engine)
Base.metadata.create_all(bind=engine)
app.include_router(company.router)
app.include_router(job.router)

@app.get("/")
def read_root():
    return {"HELLO": "WORLD"}

@app.get("/about")
def read_about():
    return{"about":"this is about page"}

@app.get("/contact")
def read_contact():
    return{"contact":"click here to contact"}