
from pydantic import BaseModel, EmailStr
from sqlmodel import SQLModel, Field

# Customer models
class CustomerBase(SQLModel):
    name: str = Field(default=None)
    description: str | None = Field(default=None)
    email: EmailStr = Field(default=None)
    age: int = Field(default=None)

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(SQLModel):
    name: str | None = None
    description: str | None = None
    email: EmailStr | None = None
    age: int | None = None

class Customer(CustomerBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class CustomerDeleteResponse(BaseModel):
    message: str = Field(default=None)
    customer: Customer = Field(default=None)

# Transaction model
class Transaction(BaseModel):
    id: int
    ammount: int
    description: str

class Invoice(BaseModel):
    id: int
    customer: Customer
    transactions: list[Transaction]
    total: int

    @property
    def ammount_total(self):
        return sum(transaction.ammount for transaction in self.transactions)
