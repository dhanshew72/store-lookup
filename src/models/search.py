from pydantic import BaseModel, Field


class SearchIn(BaseModel):
    product_id: str = Field(..., description='id of the product found on Lowe\'s search page', min_length=10, max_length=10)
    zipcode: str = Field(..., description='zipcode of location to search for product', regex='^[0-9]{5}(?:-[0-9]{4})?$')
    max_stores: int = Field(default=3, description='max number of stores being searched', ge=1, le=5)
