from gendiff.formaters._json._json import _json
from gendiff.gendiff import generate_diff


def test_json():
    with open('tests/fixtures/json_result_1.txt', 'r') as file:
        result = file.read()
    assert _json(generate_diff('gendiff/parsers/file1.json', 'gendiff/parsers/file2.json', 'json')) == result