# SDET

## Структура проекта

- data - Директория для тестовых данных
- pages - Директория для POM страниц
- tests - Директория для тестов
- reports - Директория для отчетов Allure (будет создана автоматически) 
- conftest.py - Фикстуры и конфигурация pytest 
- requirements.txt - Файл с зависимостями проекта

### Запуск тестов

pytest

### Хранения отчетов Allure:

pytest --alluredir=reports
allure serve reports (Эта команда сгенерирует отчет и откроет его в вашем браузере по умолчанию)

### Для генерации отчета в виде статических файлов:
allure generate reports -o allure-report
