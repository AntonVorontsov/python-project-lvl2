install:
	poetry install

#Запуск программ
gendiff:
	poetry run gendiff 'gendiff/parsers/file1.json' 'gendiff/parsers/file2.json'

# Сборка проекта в whl файл
build:
	poetry build

# Публикация в PyPI (иммитация)
publish:
	poetry publish --dry-run

# Установка wheel файла
package-install:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff tests/ --cov-report xml