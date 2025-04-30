from typing import List
from pydantic import BaseModel


class ProductList(BaseModel):
    Name: str
    NormalPrice: str
    SpecialPrice: str
    Brand: str
    ImageList: List[str]
    MainImageUrl: str
    Category: List[str]
    AvgRating: float
    ReviewCount: int
    ProductUrl: str
    Seller: str

class DataResponse(BaseModel):
    items: List[ProductList]