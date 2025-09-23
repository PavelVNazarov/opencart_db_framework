
pytest tests/test_customer.py -v \
  --host=localhost \
  --port=3306 \
  --database=opencart_db \
  --user=root \
  --password=your_password
```

## Структура проекта
- `tests/` - тестовые файлы
- `lib/` - библиотеки для работы с БД
- `conftest.py` - конфигурация pytest
- `requirements.txt` - зависимости проекта