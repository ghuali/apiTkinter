from models.dimensions import Dimensions
from review import Reviews
from meta import Meta
from typing import List

class Product():
    id : int
    title : str
    description : str
    category : str
    price : float
    discountPercentage : float
    rating : float
    stock : int
    tags : List[str]
    brand : str
    sku : str
    weight : int
    dimension : List[Dimensions]
    warrantlyInfo : str
    shippingInfo : str
    availabilityStatus : str
    reviews : List[Reviews]
    returnPolicy : str
    minimunOrder : int
    meta : List[Meta]
    images : str
    thumbnail : str