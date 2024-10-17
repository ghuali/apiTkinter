from importlib.metadata import metadata

from models.dimensions import Dimensions
from review import Review
from meta import Meta
from typing import List
from dataclasses import dataclass, field


@dataclass
class Product():
    id : int
    title : str
    description : str
    category : str
    price : float
    discount_percentage : float = field(metadata={'alias':'discountPercentage'})
    rating : float
    stock : int
    tags : List[str]
    brand : str
    sku : str
    weight : int
    dimension : List[Dimensions]
    warrantly_info : str = field(metadata={'alias':'warrantyInformation'})
    shipping_info : str = field(metadata={'alias':'shippingInfo'})
    availability_status : str = field(metadata={'alias':'availabilityStatus'})
    reviews : List[Review]
    returnPolicy : str
    minimunOrder : int
    meta : List[Meta]
    images : str
    thumbnail : str
    brand : str = None