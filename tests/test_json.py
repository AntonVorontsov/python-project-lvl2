from gendiff.formaters._json._json import _json
from gendiff.gendiff import generate_diff


def test_json():
    with open('/Users/antonvorontsov/PycharmProjects/python-project-lvl2/tests/fixtures/json_result.txt', 'r') as file:
        result = file.read()
    assert _json(generate_diff('/Users/antonvorontsov/PycharmProjects/python-project-lvl2/gendiff/parsers/file1.json', '/Users/antonvorontsov/PycharmProjects/python-project-lvl2/gendiff/parsers/file2.json', 'json')) == result