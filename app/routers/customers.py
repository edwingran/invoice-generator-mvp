
from fastapi import APIRouter, Query, status, HTTPException
from sqlmodel import select

from models import Customer, CustomerCreate, CustomerPlan, CustomerUpdate, CustomerDeleteResponse, Plan, StatusEnum
from db import SessionDep

router = APIRouter()

@router.post("/customers", response_model=Customer, status_code=status.HTTP_201_CREATED, tags=["customers"])
async def create_customer(customer_data: CustomerCreate, session: SessionDep):
    customer = Customer.model_validate(customer_data.model_dump())
    session.add(customer)
    session.commit()
    session.refresh(customer)
    return customer

@router.get("/customers/{customer_id}", response_model=Customer, tags=["customers"])
async def read_customer(customer_id: int, session: SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer doesn't exist")
    return customer_db


@router.patch("/customers/{customer_id}", response_model=Customer, status_code=status.HTTP_200_OK, tags=["customers"])
async def update_customer(customer_id: int, customer_data: CustomerUpdate, session: SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer doesn't exist")
    
    customer_data_dict = customer_data.model_dump(exclude_unset=True)
    customer_db.sqlmodel_update(customer_data_dict)
    session.add(customer_db)
    session.commit()
    session.refresh(customer_db)
    return customer_db


@router.delete("/customers/{customer_id}", response_model=CustomerDeleteResponse, tags=["customers"])
async def delete_customer(customer_id: int, session: SessionDep):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer doesn't exist")
    delete_customer = customer_db
    session.delete(customer_db)
    session.commit()
    return  {
        "message": "Customer deleted",
        "customer": customer_db
    }

@router.get("/customers", response_model=list[Customer], tags=["customers"])
async def list_customer(session: SessionDep):
    customers = session.exec(select(Customer)).all()
    return customers

@router.post("/customers/{customer_id}/plans/{plan_id}")
async def subscribe_customer_to_plan(customer_id: int, plan_id: int, session: SessionDep, plan_status: StatusEnum = Query()):
    customer_db = session.get(Customer, customer_id)
    plan_db = session.get(Plan, plan_id)

    if not customer_db or not plan_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="The Customer or Plan doesn't exist"
            )
    customer_plan_db = CustomerPlan(plan_id=plan_db.id, customer_id=customer_db.id, status=plan_status)
    session.add(customer_plan_db)
    session.commit()
    session.refresh(customer_plan_db)
    return customer_plan_db

@router.get("/customers/{customer_id}/plans")
async def list_customer_to_plan(customer_id: int, session: SessionDep, plan_status: StatusEnum = Query()):
    customer_db = session.get(Customer, customer_id)
    if not customer_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Customer hasn't plans")
    
    query = select(CustomerPlan).where(CustomerPlan.customer_id == customer_id).where(CustomerPlan.status == plan_status)
    plans = session.exec(query).all()
    return plans