import pytest
from gendiff.gendiff import generate_diff


@pytest.mark.parametrize('test_input,expected',[
    (('gendiff/parsers/file1.yaml', 'gendiff/parsers/file2.yaml', 'stylish'), 'tests/fixtures/result_stylish'),
    (('gendiff/parsers/file1.json', 'gendiff/parsers/file2.json', 'json'), 'tests/fixtures/result_json'),
    (('gendiff/parsers/file1.json', 'gendiff/parsers/file2.yaml', 'plain'), 'tests/fixtures/result_plain')
])


def test_output(test_input, expected):
    with open(expected, 'r') as file:
        result = file.read()

    assert generate_diff(*test_input) == result