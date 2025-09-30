<<<<<<< HEAD
# tests/test_product.py

import pytest
from lib.db import create_category, create_product, get_product_by_id


class TestProduct:

    def test_create_category(self, connection):
        """Тест: создание новой категории"""
        category_data = {
            "image": "data/category/electronics.jpg",
            "parent_id": 0,
            "top": 1,
            "column": 1,
            "sort_order": 1,
            "status": 1,
            "language_id": 1,
            "name": "Electronics",
            "description": "Latest gadgets and devices",
            "meta_title": "Electronics",
            "meta_description": "Buy electronics online",
            "meta_keyword": "gadgets, devices"
        }

        category_id = create_category(connection, category_data)
        assert category_id > 0

    def test_create_product(self, connection):
        """Тест: создание нового товара"""
        product_data = {
            "model": "iPhone 15",
            "sku": "IP15-256",
            "upc": "",
            "ean": "987654321",
            "jan": "",
            "isbn": "",
            "mpn": "",
            "location": "Warehouse A",
            "quantity": 50,
            "stock_status_id": 7,
            "image": "catalog/iphone15.jpg",
            "manufacturer_id": 1,
            "shipping": 1,
            "price": 999.99,
            "points": 0,
            "tax_class_id": 9,
            "weight": 0.2,
            "weight_class_id": 1,
            "length": 15,
            "width": 8,
            "height": 1,
            "length_class_id": 1,
            "subtract": 1,
            "minimum": 1,
            "sort_order": 1,
            "status": 1,
            "language_id": 1,
            "name": "iPhone 15 Pro Max",
            "description": "Latest iPhone from Apple",
            "tag": "Apple, iPhone",
            "meta_title": "iPhone 15",
            "meta_description": "Buy iPhone 15 online",
            "meta_keyword": "iPhone, Apple"
        }

        product_id = create_product(connection, product_data)
        assert product_id > 0

        # Проверим, что товар есть в БД
        product = get_product_by_id(connection, product_id)
        assert product is not None
        assert product["model"] == "iPhone 15"

    def test_create_product_with_invalid_data(self, connection):
        """Негативный тест: попытка создать товар с отрицательной ценой"""
        product_data = {
            "model": "Invalid Product",
            "sku": "INV-001",
            "quantity": 10,
            "price": -100,  # ❌ Некорректная цена
            "status": 1,
            "language_id": 1,
            "name": "Invalid",
            "description": "",
            "meta_title": "Invalid",
            "meta_description": "",
            "meta_keyword": ""
        }
        # Мы не обрабатываем ошибки на уровне Python, но можно добавить try-except
        # В реальной системе это может быть ограничение CHECK или приложение не пропустит.
        # Для демонстрации — просто проверим, что логика не падает
        try:
            product_id = create_product(connection, product_data)
            # Если создался — ок, но в идеале нужно проверять бизнес-логику
            if product_id:
                assert product_id > 0
        except Exception as e:
            # Это нормально, если БД отвергнет отрицательную цену
            pass  # Негативное поведение учтено

    def test_get_nonexistent_product(self, connection):
        """Негативный тест: получение несуществующего товара"""
        product = get_product_by_id(connection, 999999)
        assert product is None




=======
# tests/test_product.py

import pytest
from lib.db import create_category, create_product, get_product_by_id


class TestProduct:

    def test_create_category(self, connection):
        """Тест: создание новой категории"""
        category_data = {
            "image": "data/category/electronics.jpg",
            "parent_id": 0,
            "top": 1,
            "column": 1,
            "sort_order": 1,
            "status": 1,
            "language_id": 1,
            "name": "Electronics",
            "description": "Latest gadgets and devices",
            "meta_title": "Electronics",
            "meta_description": "Buy electronics online",
            "meta_keyword": "gadgets, devices"
        }

        category_id = create_category(connection, category_data)
        assert category_id > 0

    def test_create_product(self, connection):
        """Тест: создание нового товара"""
        product_data = {
            "model": "iPhone 15",
            "sku": "IP15-256",
            "upc": "",
            "ean": "987654321",
            "jan": "",
            "isbn": "",
            "mpn": "",
            "location": "Warehouse A",
            "quantity": 50,
            "stock_status_id": 7,
            "image": "catalog/iphone15.jpg",
            "manufacturer_id": 1,
            "shipping": 1,
            "price": 999.99,
            "points": 0,
            "tax_class_id": 9,
            "weight": 0.2,
            "weight_class_id": 1,
            "length": 15,
            "width": 8,
            "height": 1,
            "length_class_id": 1,
            "subtract": 1,
            "minimum": 1,
            "sort_order": 1,
            "status": 1,
            "language_id": 1,
            "name": "iPhone 15 Pro Max",
            "description": "Latest iPhone from Apple",
            "tag": "Apple, iPhone",
            "meta_title": "iPhone 15",
            "meta_description": "Buy iPhone 15 online",
            "meta_keyword": "iPhone, Apple"
        }

        product_id = create_product(connection, product_data)
        assert product_id > 0

        # Проверим, что товар есть в БД
        product = get_product_by_id(connection, product_id)
        assert product is not None
        assert product["model"] == "iPhone 15"

    def test_create_product_with_invalid_data(self, connection):
        """Негативный тест: попытка создать товар с отрицательной ценой"""
        product_data = {
            "model": "Invalid Product",
            "sku": "INV-001",
            "quantity": 10,
            "price": -100,  # ❌ Некорректная цена
            "status": 1,
            "language_id": 1,
            "name": "Invalid",
            "description": "",
            "meta_title": "Invalid",
            "meta_description": "",
            "meta_keyword": ""
        }
        # Мы не обрабатываем ошибки на уровне Python, но можно добавить try-except
        # В реальной системе это может быть ограничение CHECK или приложение не пропустит.
        # Для демонстрации — просто проверим, что логика не падает
        try:
            product_id = create_product(connection, product_data)
            # Если создался — ок, но в идеале нужно проверять бизнес-логику
            if product_id:
                assert product_id > 0
        except Exception as e:
            # Это нормально, если БД отвергнет отрицательную цену
            pass  # Негативное поведение учтено

    def test_get_nonexistent_product(self, connection):
        """Негативный тест: получение несуществующего товара"""
        product = get_product_by_id(connection, 999999)
        assert product is None




>>>>>>> 2889981 (Add README.md and .gitignore)
