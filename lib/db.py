<<<<<<< HEAD
# lib/db.py
import pymysql

def create_customer(connection, customer_data: dict) -> int:
    """
    Создаёт нового клиента в таблице oc_customer.
    Возвращает ID созданного клиента.
    """
    sql = """
    INSERT INTO oc_customer (
        customer_group_id, store_id, language_id, firstname, lastname,
        email, telephone, password, salt, cart, wishlist,
        newsletter, address_id, ip, status, approved,
        token, code, date_added
    ) VALUES (
        %(customer_group_id)s, %(store_id)s, %(language_id)s, %(firstname)s, %(lastname)s,
        %(email)s, %(telephone)s, %(password)s, %(salt)s, %(cart)s, %(wishlist)s,
        %(newsletter)s, %(address_id)s, %(ip)s, %(status)s, %(approved)s,
        %(token)s, %(code)s, %(date_added)s
    )
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, customer_data)
        customer_id = cursor.lastrowid
    connection.commit()
    return customer_id


def get_customer_by_id(connection, customer_id: int):
    """
    Возвращает данные клиента по ID.
    """
    sql = "SELECT * FROM oc_customer WHERE customer_id = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql, (customer_id,))
        return cursor.fetchone()


def update_customer(connection, customer_id: int, update_data: dict):
    """
    Обновляет данные клиента.
    Возвращает количество затронутых строк (0 или 1).
    """
    set_clause = ", ".join([f"{key} = %({key})s" for key in update_data.keys()])
    sql = f"UPDATE oc_customer SET {set_clause} WHERE customer_id = %(customer_id)s"
    update_data['customer_id'] = customer_id

    with connection.cursor() as cursor:
        cursor.execute(sql, update_data)
        affected = cursor.rowcount
    connection.commit()
    return affected


def delete_customer(connection, customer_id: int) -> int:
    """
    Удаляет клиента по ID.
    Возвращает количество удалённых строк (0 или 1).
    """
    sql = "DELETE FROM oc_customer WHERE customer_id = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql, (customer_id,))
        affected = cursor.rowcount
    connection.commit()
    return affected

# lib/db.py

def create_category(connection, category_data: dict) -> int:
    """Создаёт новую категорию и возвращает её ID."""
    sql = """
    INSERT INTO oc_category (
        image, parent_id, top, column, sort_order, status, date_added, date_modified
    ) VALUES (%(image)s, %(parent_id)s, %(top)s, %(column)s, %(sort_order)s, %(status)s, NOW(), NOW())
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, category_data)
        category_id = cursor.lastrowid

    # Вставляем языкозависимые данные в oc_category_description
    desc_sql = """
    INSERT INTO oc_category_description (category_id, language_id, name, description, meta_title, meta_description, meta_keyword)
    VALUES (%(category_id)s, %(language_id)s, %(name)s, %(description)s, %(meta_title)s, %(meta_description)s, %(meta_keyword)s)
    """
    category_data['category_id'] = category_id
    with connection.cursor() as cursor:
        cursor.execute(desc_sql, category_data)

    connection.commit()
    return category_id

def create_product(connection, product_data: dict) -> int:
    """Создаёт новый товар и возвращает его ID."""
    sql = """
    INSERT INTO oc_product (
        model, sku, upc, ean, jan, isbn, mpn, location, quantity, stock_status_id,
        image, manufacturer_id, shipping, price, points, tax_class_id, date_available,
        weight, weight_class_id, length, width, height, length_class_id, subtract,
        minimum, sort_order, status, viewed, date_added, date_modified
    ) VALUES (
        %(model)s, %(sku)s, %(upc)s, %(ean)s, %(jan)s, %(isbn)s, %(mpn)s, %(location)s,
        %(quantity)s, %(stock_status_id)s, %(image)s, %(manufacturer_id)s, %(shipping)s,
        %(price)s, %(points)s, %(tax_class_id)s, NOW(), %(weight)s, %(weight_class_id)s,
        %(length)s, %(width)s, %(height)s, %(length_class_id)s, %(subtract)s,
        %(minimum)s, %(sort_order)s, %(status)s, 0, NOW(), NOW()
    )
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, product_data)
        product_id = cursor.lastrowid

    # Описание товара
    desc_sql = """
    INSERT INTO oc_product_description (product_id, language_id, name, description, tag, meta_title, meta_description, meta_keyword)
    VALUES (%(product_id)s, %(language_id)s, %(name)s, %(description)s, %(tag)s, %(meta_title)s, %(meta_description)s, %(meta_keyword)s)
    """
    product_data['product_id'] = product_id
    with connection.cursor() as cursor:
        cursor.execute(desc_sql, product_data)

    connection.commit()
    return product_id

def get_product_by_id(connection, product_id: int):
    """Возвращает данные товара по ID."""
    sql = "SELECT * FROM oc_product WHERE product_id = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql, (product_id,))
        return cursor.fetchone()

def delete_category(connection, category_id: int) -> int:
    """Удаляет категорию и её описание."""
    with connection.cursor() as cursor:
        # Сначала удаляем описание
        cursor.execute("DELETE FROM oc_category_description WHERE category_id = %s", (category_id,))
        # Затем саму категорию
        cursor.execute("DELETE FROM oc_category WHERE category_id = %s", (category_id,))
        affected = cursor.rowcount
    connection.commit()
    return affected


def delete_product(connection, product_id: int) -> int:
    """Удаляет товар, его описание и связи."""
    with connection.cursor() as cursor:
        # Удаляем связи с категориями и другими таблицами
        cursor.execute("DELETE FROM oc_product_to_category WHERE product_id = %s", (product_id,))
        cursor.execute("DELETE FROM oc_product_description WHERE product_id = %s", (product_id,))
        # Удаляем сам товар
        cursor.execute("DELETE FROM oc_product WHERE product_id = %s", (product_id,))
        affected = cursor.rowcount
    connection.commit()
    return affected

=======
# lib/db.py
# lib/db.py
import pymysql


def create_customer(connection, customer_data: dict) -> int:
    """
    Создаёт нового клиента в таблице oc_customer.
    Возвращает ID созданного клиента.
    """
    sql = """
    INSERT INTO oc_customer (
        customer_group_id, store_id, language_id, firstname, lastname,
        email, telephone, password, salt, cart, wishlist,
        newsletter, address_id, ip, status, approved,
        token, code, date_added
    ) VALUES (
        %(customer_group_id)s, %(store_id)s, %(language_id)s, %(firstname)s, %(lastname)s,
        %(email)s, %(telephone)s, %(password)s, %(salt)s, %(cart)s, %(wishlist)s,
        %(newsletter)s, %(address_id)s, %(ip)s, %(status)s, %(approved)s,
        %(token)s, %(code)s, %(date_added)s
    )
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, customer_data)
        customer_id = cursor.lastrowid
    connection.commit()
    return customer_id


def get_customer_by_id(connection, customer_id: int):
    """
    Возвращает данные клиента по ID.
    """
    sql = "SELECT * FROM oc_customer WHERE customer_id = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql, (customer_id,))
        return cursor.fetchone()


def update_customer(connection, customer_id: int, update_data: dict):
    """
    Обновляет данные клиента.
    Возвращает количество затронутых строк (0 или 1).
    """
    set_clause = ", ".join([f"{key} = %({key})s" for key in update_data.keys()])
    sql = f"UPDATE oc_customer SET {set_clause} WHERE customer_id = %(customer_id)s"
    update_data['customer_id'] = customer_id

    with connection.cursor() as cursor:
        cursor.execute(sql, update_data)
        affected = cursor.rowcount
    connection.commit()
    return affected


def delete_customer(connection, customer_id: int) -> int:
    """
    Удаляет клиента по ID.
    Возвращает количество удалённых строк (0 или 1).
    """
    sql = "DELETE FROM oc_customer WHERE customer_id = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql, (customer_id,))
        affected = cursor.rowcount
    connection.commit()
    return affected

# lib/db.py

def create_category(connection, category_data: dict) -> int:
    """Создаёт новую категорию и возвращает её ID."""
    sql = """
    INSERT INTO oc_category (
        image, parent_id, top, column, sort_order, status, date_added, date_modified
    ) VALUES (%(image)s, %(parent_id)s, %(top)s, %(column)s, %(sort_order)s, %(status)s, NOW(), NOW())
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, category_data)
        category_id = cursor.lastrowid

    # Вставляем языкозависимые данные в oc_category_description
    desc_sql = """
    INSERT INTO oc_category_description (category_id, language_id, name, description, meta_title, meta_description, meta_keyword)
    VALUES (%(category_id)s, %(language_id)s, %(name)s, %(description)s, %(meta_title)s, %(meta_description)s, %(meta_keyword)s)
    """
    category_data['category_id'] = category_id
    with connection.cursor() as cursor:
        cursor.execute(desc_sql, category_data)

    connection.commit()
    return category_id

def create_product(connection, product_data: dict) -> int:
    """Создаёт новый товар и возвращает его ID."""
    sql = """
    INSERT INTO oc_product (
        model, sku, upc, ean, jan, isbn, mpn, location, quantity, stock_status_id,
        image, manufacturer_id, shipping, price, points, tax_class_id, date_available,
        weight, weight_class_id, length, width, height, length_class_id, subtract,
        minimum, sort_order, status, viewed, date_added, date_modified
    ) VALUES (
        %(model)s, %(sku)s, %(upc)s, %(ean)s, %(jan)s, %(isbn)s, %(mpn)s, %(location)s,
        %(quantity)s, %(stock_status_id)s, %(image)s, %(manufacturer_id)s, %(shipping)s,
        %(price)s, %(points)s, %(tax_class_id)s, NOW(), %(weight)s, %(weight_class_id)s,
        %(length)s, %(width)s, %(height)s, %(length_class_id)s, %(subtract)s,
        %(minimum)s, %(sort_order)s, %(status)s, 0, NOW(), NOW()
    )
    """
    with connection.cursor() as cursor:
        cursor.execute(sql, product_data)
        product_id = cursor.lastrowid

    # Описание товара
    desc_sql = """
    INSERT INTO oc_product_description (product_id, language_id, name, description, tag, meta_title, meta_description, meta_keyword)
    VALUES (%(product_id)s, %(language_id)s, %(name)s, %(description)s, %(tag)s, %(meta_title)s, %(meta_description)s, %(meta_keyword)s)
    """
    product_data['product_id'] = product_id
    with connection.cursor() as cursor:
        cursor.execute(desc_sql, product_data)

    connection.commit()
    return product_id

def get_product_by_id(connection, product_id: int):
    """Возвращает данные товара по ID."""
    sql = "SELECT * FROM oc_product WHERE product_id = %s"
    with connection.cursor() as cursor:
        cursor.execute(sql, (product_id,))
        return cursor.fetchone()

>>>>>>> 2889981 (Add README.md and .gitignore)
