from enum import Enum


class ProductType(Enum):
    TYPE_A = "type_a"
    TYPE_B = "type_b"
    TYPE_C = "type_c"


class Product:
    def __init__(self, name: str, product_type: ProductType, price: int):
        self.name = name
        self.product_type = product_type
        self.price = price


class NotEnoughMoney(Exception):
    pass


class Client:
    def __init__(self, name: str, wallet: int):
        self.name = name
        self.wallet = wallet

    def buy_product(self, product: Product, quantity: int = 1):
        if self.wallet < product.price:
            raise NotEnoughMoney("Solde insuffisant !")
        print("Produit acheté !")
        self.wallet = self.wallet - product.price * quantity
