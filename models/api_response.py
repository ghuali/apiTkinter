from dataclasses import dataclass
from itertools import product

@dataclass
class APIresponse():
    products : list[product]
    total : float
    skip : int
    limit : int
