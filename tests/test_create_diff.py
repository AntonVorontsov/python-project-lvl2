import pytest
from gendiff.gendiff import create_diff


def test_create_diff():
    with open('/Users/antonvorontsov/PycharmProjects/python-project-lvl2/tests/fixtures/create_diff_result.txt', 'r') as file:
        result = file.read()

    assert str(create_diff('/Users/antonvorontsov/PycharmProjects/python-project-lvl2/gendiff/parsers/file1.json', '/Users/antonvorontsov/PycharmProjects/python-project-lvl2/gendiff/parsers/file2.json')) == result
    # assert str(create_diff('gendiff/parsers/file1.yml', 'gendiff/parsers/file2.yml')) == result
    # assert str(create_diff('gendiff/parsers/file1.json', 'gendiff/parsers/file2.yml')) == result


def test_exception():
    # Добавляем: as e. e – произвольное имя переменной содержащей исключение
    with pytest.raises(Exception) as e:
        create_diff()

    assert str(e.value) == "create_diff() missing 2 required positional arguments: 'path_file1' and 'path_file2'"