from gendiff.formaters.plain.plain import plain
from gendiff.gendiff import generate_diff


def test_plain():
    with open('tests/fixtures/result_plain_1', 'r') as file:
        result = file.read()

    assert plain(generate_diff('gendiff/parsers/file_1.json', 'gendiff/parsers/file_2.json', 'plain')) == result
    assert plain(generate_diff('gendiff/parsers/file_1.yml', 'gendiff/parsers/file_2.yml', 'plain')) == result