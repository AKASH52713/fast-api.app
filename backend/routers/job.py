from fastapi import APIRouter , HTTPException, Depends, status
from sqlalchemy.orm import Session
from schemas.job import JobCreate, JobUpdate, JobResponse
from models.job import Job
from database import get_db


router= APIRouter(prefix="/job",tags=["job"])
jobs=[]

@router.post("/" ,status_code=status.HTTP_201_CREATED, response_model=JobResponse)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    db_job = Job(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.get("/" ,status_code=status.HTTP_200_OK, response_model=JobResponse)
def get_all_job(db: Session = Depends(get_db)):
    jobs= db.query(Job).all()
    return jobs

@router.get("/{job_id}" ,status_code=status.HTTP_200_OK, response_model=JobResponse)
def get_job(job_id: int, db: Session = Depends(get_db)):
    db_job = db.get(Job, job_id)
    if not db_job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    return db_job


@router.put("/{job_id}",response_model=JobResponse)
def update_job(job_id: int, job: JobUpdate, db: Session = Depends(get_db)):
    db_job = db.get(Job, Job_id)
    if not db_job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    for field, value in job.dict(exclude_unset=True).items():
        setattr(db_job, field, value)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.delete("/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    db_job = db.get(Job, job_id)
    if not db_job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    db.delete(db_job)
    db.commit()
    return {"ok": True}


# @router.get("/")
# def read_job():
#     return {"job":"Job root"}

# @router.get("/{job_id}")
# def read_job(job_id: int):
#     return {"job_id": job_id}