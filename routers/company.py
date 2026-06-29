from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from schemas.company import CompanyCreate, CompanyUpdate, CompanyResponse
from database import get_db
from models.company import Company

router = APIRouter(prefix="/company", tags=["company"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CompanyResponse)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    db_company = Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[CompanyResponse])
def get_all_company(db: Session = Depends(get_db)):
    compsnies= db.query(Company).all()
    return compsnies


@router.get("/{company_id}", status_code=status.HTTP_200_OK, response_model=CompanyResponse)
def get_company(company_id: int, db: Session = Depends(get_db)):
    db_company = db.get(Company, company_id)
    if not db_company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    return db_company

@router.put("/{company_id}", response_model=CompanyResponse)



def update_company(company_id: int, company: CompanyUpdate, db: Session = Depends(get_db)):
    db_company = db.get(Company, company_id)
    if not db_company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    for field, value in company.dict(exclude_unset=True).items():
        setattr(db_company, field, value)
    db.commit()
    db.refresh(db_company)
    return db_company

@router.delete("/{company_id}")
def delete_company(company_id: int, db: Session = Depends(get_db)):
    db_company = db.get(Company, company_id)
    if not db_company:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Company not found")
    db.delete(db_company)
    db.commit()
    return {"ok": True}
# @router.get("/")
# def read_company():
#     return {"company":"Company root"}

# @router.get("/{company_id}")
# def read_company(company_id:int):
#     return {"company_id": company_id}
        