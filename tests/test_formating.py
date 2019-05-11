# -*- coding: utf-8 -*-

from .context import myapp

import unittest
from unittest import mock

# Unit tests are used to test the if the expected output is given
# Mock tests are used to test if a mocked object is being called in the right way


class BasicTestSuite(unittest.TestCase):

    def setUp(self):
        self.h1_formater = myapp.TagTextFormater('H1')
        self.div_formater = myapp.TagTextFormater('DIV')
        self.html_formater = myapp.HTMLDocumentFormater(self.h1_formater, self.div_formater)
        self.page_formater = myapp.WebPageHTMLDocumentFormater('Test', self.h1_formater, self.div_formater)
        self.document = myapp.Document('HELLO', 'WORLD')

    def test_tag_text_formater(self):
        """
        Test wheter TagTextFormater formats correctly.
        """
        ret = self.h1_formater.format('HELLO')
        self.assertEqual(ret, '<H1>HELLO</H1>')

    def test_html_document_formater(self):
        """
        Test wheter HTMLDocumentFormater formats correctly.
        """
        ret = self.html_formater.format(self.document)
        self.assertEqual(ret, '<H1>HELLO</H1><br><DIV>WORLD</DIV>')

    def test_page_formater(self):
        """
        Test wheter WebPageHTMLDocumentFormater formats correctly.
        """
        ret = self.page_formater.format(self.document)
        self.assertEqual(ret, '<head>Test</head><body><H1>HELLO</H1><br><DIV>WORLD</DIV></body>')

    def test_html_formater_title_call(self):
        """
        Test whether HTMLDocumentFormater calls the title formater with correct input.
        """
        mock_title_formater = mock.Mock()
        mock_content_formater = mock.Mock()

        html_formater = myapp.HTMLDocumentFormater(mock_title_formater, mock_content_formater)
        html_formater.format(self.document)

        mock_title_formater.format.assert_called_with('HELLO')

    def test_html_formater_content_call(self):
        """
        Test whether HTMLDocumentFormater calls the content formater with correct input.
        """
        mock_title_formater = mock.Mock()
        mock_content_formater = mock.Mock()

        html_formater = myapp.HTMLDocumentFormater(mock_title_formater, mock_content_formater)
        html_formater.format(self.document)

        mock_content_formater.format.assert_called_with('WORLD')


if __name__ == '__main__':
    unittest.main()