from fastapi import APIRouter, status, HTTPException
from sqlmodel import select

from models import Transaction
from db import SessionDep

router = APIRouter()


@router.post("/transactions", tags=["transactions"])
async def create_transaction(transaction_data: Transaction):

    return transaction_data