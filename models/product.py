from dataclasses import dataclass

from models.dimensions import Dimensions
from models.review import Review
from models.meta import Meta
from typing import List

@dataclass
class Product:
    id : int
    title : str
    description : str
    category : str
    price : float
    discount_percentage : float
    rating : float
    stock : int
    tags : List[str]
    sku : str
    weight : int
    dimensions : Dimensions
    warranty_information : str
    shipping_information : str
    availability_status : str
    reviews : List[Review]
    return_policy : str
    minimum_order_quantity : int
    meta : Meta
    images : List[str]
    thumbnail : str
    brand : str = None