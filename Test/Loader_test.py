import unittest

from Loader import Load,PDF_READERS

class TestLoadFunction(unittest.TestCase):
    def test_Load_PyPDF2_PageDetection(self):
        self.assertEqual(len(Load(PDF_READERS.PyPdf2,r"SampleDocs/sample-1.pdf").pages),2)
    
if __name__ == '__main__':
    unittest.main()