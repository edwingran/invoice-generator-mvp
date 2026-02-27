from fastapi import FastAPI
from datetime import datetime

import zoneinfo
from db import create_all_tables
from sqlmodel import select
from .routers import plans, customers, transactions, invoices


app = FastAPI(lifespan=create_all_tables)
app.include_router(customers.router)
app.include_router(transactions.router)
app.include_router(invoices.router)
app.include_router(plans.router)

@app.get("/")
async def root():
    return{"message" : "invoice-generator-mvp"}

country_timezones = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "AR": "America/Argentina/Buenos_Aires",
    "BR": "America/Sao_Paulo",
    "PE": "America/Lima",
}

@app.get("/time/{iso_code}")
async def time(iso_code: str):
    # Co --> CO
    iso = iso_code.upper()
    timezone_str = country_timezones.get(iso)
    tz = zoneinfo.ZoneInfo(timezone_str)
    return{"time" : datetime.now(tz)}

#db_customer: list[Customer] = []


