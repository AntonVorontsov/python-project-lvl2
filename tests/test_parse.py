from gendiff.parsers.parse import parse_json
from gendiff.parsers.parse import parse_yaml


def test_parse():
    with open('tests/fixtures/file1_result.txt', 'r') as file:
        result = file.read()
    assert str(parse_yaml('gendiff/parsers/file1.yaml')) == result

    with open('tests/fixtures/file2_result.txt', 'r') as file:
        result = file.read()
    assert str(parse_json('gendiff/parsers/file2.json')) == result
