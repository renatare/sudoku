import unittest
import os
from file_opener import *

class TestFileOpener(unittest.TestCase):
    def setUp(self):
        self.readable_file = 'files/test_file.txt'
        self.uploadable_file = 'files/test_file_upload.txt'

        self.file_opener = FileOpener()

    def test_read_from_file(self):
            contents = self.file_opener.read_from_file(self.readable_file)
            self.assertEqual([[1,2,3,4,5]], contents) 

    def test_upload_to_file(self):
        try:
            self.file_opener.upload_to_file(self.uploadable_file, '111')

            contents = self.file_opener.read_from_file(self.uploadable_file)
            self.assertEqual([[1,1,1]], contents) 
        finally:
            os.remove(self.uploadable_file)

    def test_append_to_file(self):
        try:
            self.file_opener.append_to_file(self.uploadable_file, '123')
            self.file_opener.append_to_file(self.uploadable_file, '321')

            contents = self.file_opener.read_from_file(self.uploadable_file)
            self.assertEqual([[1,2,3,3,2,1]], contents) 
        finally:
            os.remove(self.uploadable_file)

if __name__ == "__main__":
    unittest.main()
