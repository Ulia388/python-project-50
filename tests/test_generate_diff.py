import json
import os
import tempfile
import unittest

from gendiff.scripts.generate_diff import generate_diff


class TestGenerateDiff(unittest.TestCase):

    def create_temp_file(self, content):
        tmp = tempfile.NamedTemporaryFile(
            mode='w+', delete=False
        )
        json.dump(content, tmp)
        tmp.close()
        return tmp.name

    def tearDown(self):
        
        for attr in ('f1', 'f2'):
            f = getattr(self, attr, None)
            if f and os.path.exists(f):
                os.remove(f)

    def test_equal_files(self):
        data = {"a": 1, "b": "text", "c": True}
        self.f1 = self.create_temp_file(data)
        self.f2 = self.create_temp_file(data)
        expected = '''{
            a: 1
            b: text
            c: true
        }'''
        result = generate_diff(self.f1, self.f2)
        self.assertEqual(
            self.normalize_output(result),
            self.normalize_output(expected)
        )

    def normalize_output(self, output):
        
        return "\n".join(
            line.strip() for line in output.strip().splitlines()
        )   

    def test_add_key(self):
        data1 = {"a": 1}
        data2 = {"a": 1, "b": 2}
        self.f1 = self.create_temp_file(data1)
        self.f2 = self.create_temp_file(data2)
        expected = '''{
        a: 1
        + b: 2
        }'''
        result = generate_diff(self.f1, self.f2)
        self.assertEqual(
            self.normalize_output(result),
            self.normalize_output(expected)
        )

    def test_remove_key(self):
        data1 = {"a": 1, "b": 2}
        data2 = {"a": 1}
        self.f1 = self.create_temp_file(data1)
        self.f2 = self.create_temp_file(data2)
        expected = '''{
        a: 1
        - b: 2
        }'''
        result = generate_diff(self.f1, self.f2)
        self.assertEqual(
            self.normalize_output(result),
            self.normalize_output(expected)
        )

    def test_change_key_value(self):
        data1 = {"a": 1, "b": 2}
        data2 = {"a": 1, "b": 3}
        self.f1 = self.create_temp_file(data1)
        self.f2 = self.create_temp_file(data2)
        expected = '''{
        a: 1
        - b: 2
        + b: 3
        }'''
        result = generate_diff(self.f1, self.f2)
        self.assertEqual(
            self.normalize_output(result),
            self.normalize_output(expected)
        )

    if __name__ == '__main__':
        unittest.main()