# conftest.py
import pytest
import pymysql


def pytest_addoption(parser):
    parser.addoption(
        "--host", action="store", default="localhost", help="Database host"
    )
    parser.addoption(
        "--port", action="store", default=3306, type=int, help="Database port"
    )
    parser.addoption(
        "--database", action="store", required=True, help="Database name"
    )
    parser.addoption(
        "--user", action="store", required=True, help="Database user"
    )
    parser.addoption(
        "--password", action="store", default="", help="Database password"
    )


@pytest.fixture(scope="session")
def connection(request):
    host = request.config.getoption("--host")
    port = request.config.getoption("--port")
    database = request.config.getoption("--database")
    user = request.config.getoption("--user")
    password = request.config.getoption("--password")

    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=False
    )

    yield conn

    conn.close()


