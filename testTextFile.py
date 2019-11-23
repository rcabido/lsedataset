import unittest
from sample import textFile
import os, fnmatch

class TestTextFile(unittest.TestCase):
    def test_list_not_null(self):
        """
        Test that the module textFile return a not null list
        """

        auxTest = textFile.TextFile('ej.txt')
        list = auxTest.listUrls()
        self.assertTrue(len(list)>1)
    
    def test_filename_wrong(self):
        filename = "banana"
        auxTest = textFile.TextFile(filename)
        with self.assertRaises(FileNotFoundError):
            list = auxTest.listUrls()

    def test_filename_null(self):
        with self.assertRaises(TypeError):
           auxTest = textFile.TextFile()


if __name__ == '__main__':
    unittest.main()