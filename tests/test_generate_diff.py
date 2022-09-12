from gendiff.gendiff import generate_diff


def test_generate_diff():
    with open('tests/fixtures/result_plain_1', 'r') as file:
        plain_result = file.read()

    assert str(generate_diff('gendiff/parsers/file_1.json', 'gendiff/parsers/file_2.json', 'plain')) == plain_result
    assert str(generate_diff('gendiff/parsers/file_1.yml', 'gendiff/parsers/file_2.yml', 'plain')) == plain_result
    assert str(generate_diff('gendiff/parsers/file_1.json', 'gendiff/parsers/file_2.yml', 'plain')) == plain_result


def test_generate_diff():
    with open('tests/fixtures/result_stylish_1', 'r') as file:
        stylish_result = file.read()

    assert str(generate_diff('gendiff/parsers/file_1.json', 'gendiff/parsers/file_2.json', 'stylish')) == stylish_result
    assert str(generate_diff('gendiff/parsers/file_1.yml', 'gendiff/parsers/file_2.yml', 'stylish')) == stylish_result
    assert str(generate_diff('gendiff/parsers/file_1.json', 'gendiff/parsers/file_2.yml', 'stylish')) == stylish_result


def test_generate_diff():
    with open('tests/fixtures/result_json_1', 'r') as file:
        json_result = file.read()

    assert str(generate_diff('gendiff/parsers/file_1.json', 'gendiff/parsers/file_2.json', 'json')) == json_result
    assert str(generate_diff('gendiff/parsers/file_1.yml', 'gendiff/parsers/file_2.yml', 'json')) == json_result
    assert str(generate_diff('gendiff/parsers/file_1.json', 'gendiff/parsers/file_2.yml', 'json')) == json_result