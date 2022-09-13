from gendiff.formaters.stylish.stylish import stylish
from gendiff.gendiff import generate_diff

result = stylish(generate_diff('/Users/antonvorontsov/PycharmProjects/python-project-lvl2/gendiff/parsers/file1.yaml', '/Users/antonvorontsov/PycharmProjects/python-project-lvl2/gendiff/parsers/file2.yaml', 'stylish'))

with open('/Users/antonvorontsov/PycharmProjects/python-project-lvl2/tests/fixtures/result_stylish', 'w') as file:
    result = file.write(result)