import pytest
from gendiff.gendiff import create_diff


def test_create_diff():
    with open('tests/fixtures/create_diff_result_1.txt', 'r') as file:
        result = file.read()

    assert str(create_diff('gendiff/parsers/file_1.json', 'gendiff/parsers/file_2.json')) == result
    assert str(create_diff('gendiff/parsers/file_1.yml', 'gendiff/parsers/file_2.yml')) == result
    assert str(create_diff('gendiff/parsers/file_1.json', 'gendiff/parsers/file_2.yml')) == result


def test_exception():
    # Добавляем: as e. e – произвольное имя переменной содержащей исключение
    with pytest.raises(Exception) as e:
        create_diff()

    assert str(e.value) == "create_diff() missing 2 required positional arguments: 'path_file1' and 'path_file2'"