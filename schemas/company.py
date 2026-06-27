from pydantic import BaseModel
from typing import Optional
from .job import JobResponse 
class CompanyBase(BaseModel):
    name: str
    email : str
    phone : str

class CompanyCreate(CompanyBase):
    pass
    # name: str
    # location: str


class CompanyUpdate(CompanyBase):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

class CompanyRespomse(CompanyBase):
    id: int
    job:list[JobResponse]

    class config:
        from_attributes = True