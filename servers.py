#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

from typing import List, Optional


class Product:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą argumenty wyrażające nazwę produktu (typu str) i jego cenę (typu float) -- w takiej kolejności -- i ustawiającą atrybuty `name` (typu str) oraz `price` (typu float)

    def __init__(self, name: str, price: float):
        if any(not c.isalnum() for c in name) or len(re.split("(\d+)", name)[:-1]) != 2:
            raise ValueError
        self.name = name
        self.price = price

    def __eq__(self, other: __build_class__):
        if self.name == other.name and self.price == other.price:
            return True
        return False
        return None  # FIXME: zwróć odpowiednią wartość

    def __hash__(self):
        return hash((self.name, self.price))

    def set_name(self, name: str):
        self.name = name

    def set_price(self, price: float):
        self.price = price


class TooManyProductsFoundError:
    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.
    pass


# FIXME: Każada z poniższych klas serwerów powinna posiadać:
#   (1) metodę inicjalizacyjną przyjmującą listę obiektów typu `Product` i ustawiającą atrybut `products` zgodnie z typem reprezentacji produktów na danym serwerze,
#   (2) możliwość odwołania się do atrybutu klasowego `n_max_returned_entries` (typu int) wyrażający maksymalną dopuszczalną liczbę wyników wyszukiwania,
#   (3) możliwość odwołania się do metody `get_entries(self, n_letters)` zwracającą listę produktów spełniających kryterium wyszukiwania


class Server:
    n_max_returned_entries: int = 3

    def get_entries(self, n_letters: int = 1) -> List[Product]:
        result = []

        if self.products == "list":
            for product in self.list_products:
                letters, numbers = re.split("(\d+)", product.name)[:-1]
                if len(letters) == n_letters and 2 <= len(numbers) <= 3:
                    result.append(product)

        elif self.products == "dict":
            for product in self.dict_products.values():
                letters, numbers = re.split("(\d+)", product.name)[:-1]
                if len(letters) == n_letters and 2 <= len(numbers) <= 3:
                    result.append(product)

        if len(result) > self.n_max_returned_entries:
            raise TooManyProductsFoundError

        return result


class ListServer(Server):
    products = "list"

    def __init__(self, list_products: List[Product]):
        self.list_products = list_products


class MapServer(Server):
    products = "dict"

    def __init__(self, list_products: List[Product]):
        self.dict_products = {}
        for product in list_products:
            self.dict_products[product.name] = product


class Client:
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer

    def __init__(self, server: Server):
        self.server = server

    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        return sum([product.price for product in self.server.get_entries(n_letters)])
        raise NotImplementedError()
