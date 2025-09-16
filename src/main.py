from business import Client, Product, NotEnoughMoney, ProductType


def main():
    product1 = Product("Produit 1", ProductType.TYPE_A, 60)
    product2 = Product("Produit 2", ProductType.TYPE_B, 100)
    available_products = {
        "1": product1,
        "2": product2
    }

    firstname = input("Quel est votre prénom ?")
    client = Client(firstname, 300)
    print(f"Bonjour {firstname}, votre solde est de : {client.wallet}\n")

    client_is_online = True

    while client_is_online:
        print("Que voulez-vous acheter ?\n")
        for key, product in available_products.items():
            print(f"{key}) {product.name} - {product.product_type} ({product.price}€)\n")
        print("0) Quitter\n")
        choice = input("Votre choix ?\n")

        chosen_product = None

        if choice == "0":
            client_is_online = False
        else:
            for key, product in available_products.items():
                if choice == key:
                    chosen_product = product

        if chosen_product is not None:
            try:
                client.buy_product(chosen_product)
            except NotEnoughMoney:
                print("Pas assez d'argent")
            except Exception:
                print("Un problème est survenu")

    print("A bientôt !")


if __name__ == '__main__':
    main()
