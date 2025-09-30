<<<<<<< HEAD
# tests/test_category.py
import pytest
from lib.db import create_category, create_product


def test_assign_product_to_category(connection, created_category, created_product):
    """Тест: добавление товара в категорию через oc_product_to_category"""
    product_id = created_product
    category_id = created_category

    # Привязываем товар к категории
    sql = "INSERT INTO oc_product_to_category (product_id, category_id) VALUES (%s, %s)"
    with connection.cursor() as cursor:
        cursor.execute(sql, (product_id, category_id))
    connection.commit()

    # Проверяем, что связь есть
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM oc_product_to_category WHERE product_id = %s AND category_id = %s",
            (product_id, category_id)
        )
        link = cursor.fetchone()
        assert link is not None

=======
# test_category.py
import pytest
from lib.db import create_category, create_product, get_product_by_id
def test_assign_product_to_category(self, connection):
    """Тест: добавление товара в категорию через oc_product_to_category"""
    # Сначала создаём категорию
    category_data = {
        "image": "", "parent_id": 0, "top": 1, "column": 1, "sort_order": 1, "status": 1,
        "language_id": 1, "name": "Phones", "description": "", "meta_title": "Phones",
        "meta_description": "", "meta_keyword": ""
    }
    category_id = create_category(connection, category_data)

    # Создаём товар
    product_data = {
        "model": "Galaxy S24", "sku": "GAL-S24", "quantity": 20, "price": 899.99, "status": 1,
        "language_id": 1, "name": "Samsung Galaxy S24", "description": "", "meta_title": "S24",
        "meta_description": "", "meta_keyword": ""
    }
    product_id = create_product(connection, product_data)

    # Привязываем товар к категории
    sql = "INSERT INTO oc_product_to_category (product_id, category_id) VALUES (%s, %s)"
    with connection.cursor() as cursor:
        cursor.execute(sql, (product_id, category_id))
    connection.commit()

    # Проверяем, что связь есть
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM oc_product_to_category WHERE product_id = %s AND category_id = %s",
                       (product_id, category_id))
        link = cursor.fetchone()
        assert link is not None

>>>>>>> 2889981 (Add README.md and .gitignore)
