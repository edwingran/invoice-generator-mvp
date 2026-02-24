
from fastapi import APIRouter, status, HTTPException
from sqlmodel import select

from models import Invoice
from db import SessionDep

router = APIRouter()


@router.post("/invoices", tags=["invoices"])
async def create_invoices(invoice_data: Invoice):

    return invoice_data 