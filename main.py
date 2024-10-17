import requests
from models.api_response import APIresponse
from dataclass_wizard import fromdict
from vistas import mostrar_productos

def main():
    response = requests.get('https://dummyjson.com/products')
    data_dict = response.json()
    data_obj = fromdict(APIresponse,data_dict)
    mostrar_productos(data_obj)

main()