from gendiff.gendiff import generate_diff


def test_generate_diff():
    with open('/Users/antonvorontsov/PycharmProjects/python-project-lvl2/tests/fixtures/result_plain', 'r') as file:
        plain_result = file.read()

    assert str(generate_diff('/Users/antonvorontsov/PycharmProjects/python-project-lvl2/gendiff/parsers/file1.json', '/Users/antonvorontsov/PycharmProjects/python-project-lvl2/gendiff/parsers/file2.json', 'plain')) == plain_result
    # assert str(generate_diff('gendiff/parsers/file1.yml', 'gendiff/parsers/file2.yml', 'plain')) == plain_result
    # assert str(generate_diff('gendiff/parsers/file1.json', 'gendiff/parsers/file2.yml', 'plain')) == plain_result