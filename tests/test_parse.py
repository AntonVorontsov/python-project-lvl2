from gendiff.parsers.parse import parse_json
from gendiff.parsers.parse import parse_yaml

def test_parse():
    with open('tests/fixtures/file1_result_1.txt', 'r') as file:
        result = file.read()
    assert str(parse_yaml('gendiff/parsers/file_1.yml')) == result

    with open('tests/fixtures/file2_result_1.txt', 'r') as file:
        result = file.read()
    assert str(parse_json('gendiff/parsers/file_2.json')) == result