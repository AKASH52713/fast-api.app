from pydantic import BaseModel
from typing import Optional


class JobBase(BaseModel):
    title: str
    salary : int
    descreption : str
    company_id: int
class JobCreate(JobBase):
    pass
    # title: str
    # salary: int

class JobUpdate(JobBase):
    title: Optional[str]=None
    salary: Optional[int]=None
    description : Optional[str]=None
    company_id : Optional[int]=None

class JobResponse(JobBase):
    id : int
    company_id: int

    class Config:
        from_attributes = True