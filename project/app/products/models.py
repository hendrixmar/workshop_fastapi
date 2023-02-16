from decimal import Decimal
from typing import Annotated, Optional

from pydantic import condecimal
from pydantic.types import PositiveInt
from sqlmodel import Field, SQLModel


class ProductBase(SQLModel):
    name: str
    status: bool = Field(default=True)
    stock: PositiveInt = Field(default=0)
    description: str
    price: condecimal(ge=Decimal("0.0"), max_digits=10, decimal_places=2) = Field(
        default=0
    )


class Product(ProductBase, table=True):
    product_id: int = Field(default=None, primary_key=True)