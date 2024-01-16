# Описание фреймворка
   Для установки зависимостей и создания виртуального окружения используется менеджер версий poetry.
   Хранение кредов и управление конфигурациями окружения реализовано с помощью dynaconf.
pytest ini

### Требования для запуска
* python>=3.8
* poetry

### Установка poetry
```sh
  pip install poetry
```

# Установка зависимостей
Poetry хранит информацию о необходимых пакетах в файле pyproject.toml
```sh
cd autotests-api # Переходим в директорию autotests-api, если вдруг еще не находимся в ней
poetry install
```

# Отчётность
   
1. Установка ---
```sh
null
```
2. Смотрим отчёт:
```sh
allure serve allure_report
```

# Запуск API тестов

```sh
poetry run pytest tests/
```
или
```sh
poetry shell
pytest tests/
```
