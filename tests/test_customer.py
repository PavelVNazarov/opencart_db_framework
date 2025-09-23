# tests/test_customer.py
# tests/test_customer.py
import pytest
from lib.db import (
    create_customer,
    get_customer_by_id,
    update_customer,
    delete_customer
)
import time


# Пример данных нового клиента
CUSTOMER_DATA = {
    "customer_group_id": 1,
    "store_id": 0,
    "language_id": 1,
    "firstname": "John",
    "lastname": "Doe",
    "email": "johndoe@example.com",
    "telephone": "1234567890",
    "password": "hashed_password",  # В реальной БД — хэш!
    "salt": "abc123",
    "cart": None,
    "wishlist": None,
    "newsletter": 0,
    "address_id": 0,
    "ip": "127.0.0.1",
    "status": 1,
    "approved": 1,
    "token": "",
    "code": "",
    "date_added": time.strftime('%Y-%m-%d %H:%M:%S')
}

UPDATE_DATA = {
    "firstname": "Jane",
    "lastname": "Smith",
    "email": "jane.smith@example.com",
    "telephone": "9876543210"
}


class TestCustomer:

    def test_create_customer(self, connection):
        """Тест: создание нового клиента и проверка его наличия в БД."""
        customer_id = create_customer(connection, CUSTOMER_DATA)
        assert customer_id > 0

        customer = get_customer_by_id(connection, customer_id)
        assert customer is not None
        assert customer["firstname"] == "John"
        assert customer["email"] == "johndoe@example.com"

    def test_update_existing_customer(self, connection):
        """Тест: обновление данных существующего клиента."""
        
        customer_id = create_customer(connection, CUSTOMER_DATA)

       
        rows_affected = update_customer(connection, customer_id, UPDATE_DATA)
        assert rows_affected == 1

       
        updated = get_customer_by_id(connection, customer_id)
        assert updated["firstname"] == "Jane"
        assert updated["lastname"] == "Smith"
        assert updated["email"] == "jane.smith@example.com"
        assert updated["telephone"] == "9876543210"

    def test_update_nonexistent_customer(self, connection):
        """Негативный тест: обновление несуществующего клиента."""
        fake_id = 999999
        rows_affected = update_customer(connection, fake_id, UPDATE_DATA)
        assert rows_affected == 0

    def test_delete_existing_customer(self, connection):
        """Тест: удаление существующего клиента."""
        customer_id = create_customer(connection, CUSTOMER_DATA)

       
        rows_affected = delete_customer(connection, customer_id)
        assert rows_affected == 1

    
        customer = get_customer_by_id(connection, customer_id)
        assert customer is None

    def test_delete_nonexistent_customer(self, connection):
        """Негативный тест: удаление несуществующего клиента."""
        fake_id = 999999
        rows_affected = delete_customer(connection, fake_id)
        assert rows_affected == 0

