# tests/test_customer.py
import pytest
from lib.db import (
    create_customer,
    get_customer_by_id,
    update_customer,
    delete_customer
)


class TestCustomer:

    def test_create_customer(self, connection, unique_customer_data):
        """Тест: создание нового клиента и проверка его наличия в БД."""
        customer_id = create_customer(connection, unique_customer_data)
        assert customer_id > 0

        customer = get_customer_by_id(connection, customer_id)
        assert customer is not None
        assert customer["email"] == unique_customer_data["email"]

    def test_update_existing_customer(self, connection, created_customer, update_data):
        """Тест: обновление данных существующего клиента."""
        rows_affected = update_customer(connection, created_customer, update_data)
        assert rows_affected == 1

        updated = get_customer_by_id(connection, created_customer)
        assert updated["firstname"] == update_data["firstname"]
        assert updated["lastname"] == update_data["lastname"]
        assert updated["email"] == update_data["email"]
        assert updated["telephone"] == update_data["telephone"]

    def test_update_nonexistent_customer(self, connection, update_data):
        """Негативный тест: обновление несуществующего клиента."""
        fake_id = 999999999
        rows_affected = update_customer(connection, fake_id, update_data)
        assert rows_affected == 0

    def test_delete_existing_customer(self, connection, created_customer):
        """Тест: удаление существующего клиента."""
        rows_affected = delete_customer(connection, created_customer)
        assert rows_affected == 1

        customer = get_customer_by_id(connection, created_customer)
        assert customer is None

    def test_delete_nonexistent_customer(self, connection):
        """Негативный тест: удаление несуществующего клиента."""
        fake_id = 999999999
        rows_affected = delete_customer(connection, fake_id)
        assert rows_affected == 0
