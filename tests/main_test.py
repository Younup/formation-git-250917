import pytest

from src.business import Client, Product, NotEnoughMoney, ProductType


def test_buy_product_decrease_wallet_with_product_price():
    # given
    client = Client("Bob", 200)
    product = Product("Product 1", ProductType.TYPE_A, 50)

    # when
    client.buy_product(product)

    # then
    assert client.wallet == 150


def test_buy_product_decrease_wallet_until_empty():
    # given
    client = Client("Bob", 100)
    product = Product("Product 1", ProductType.TYPE_A, 100)

    # when
    client.buy_product(product)

    # then
    assert client.wallet == 0


def test_buy_product_should_raise_exception_when_not_enough_money():
    # given
    client = Client("Bob", 100)
    product = Product("Product 1", ProductType.TYPE_A, 200)

    # when
    with pytest.raises(NotEnoughMoney):
        client.buy_product(product)

    # then
    assert client.wallet == 100


def test_buy_product_should_decrease_wallet_for_each_quantity():
    # given
    client = Client("Bob", 200)
    product = Product("Product 1", ProductType.TYPE_A, 100)

    # when
    client.buy_product(product, 2)

    # then
    assert client.wallet == 0


def test_buy_product_should_not_set_negative_wallet_value():
    # given
    client = Client("Bob", 200)
    product = Product("Product 1", ProductType.TYPE_A, 100)

    # when
    with pytest.raises(NotEnoughMoney):
        client.buy_product(product, 4)

    # then
    assert client.wallet > 0
