import pytest

from gendiff.scripts.generate_diff import generate_diff


@pytest.mark.parametrize('file_path1, file_path2, expected', [
    ('tests/test_data/first_file.json',
     'tests/test_data/second_file.json',
     'tests/test_data/expected.json.txt'),
    ('tests/test_data/file1.yaml',
     'tests/test_data/file2.yaml',
     'tests/test_data/expected.yaml.txt')
])
def test_generate_diff(file_path1, file_path2, expected):
    diff = generate_diff(file_path1, file_path2)
    with open(expected, encoding='utf-8') as f:
        expected_content = f.read().strip()
    assert diff.strip() == expected_content
