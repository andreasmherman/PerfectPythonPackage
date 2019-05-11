# -*- coding: utf-8 -*-

from . import decorators

# Follow SOLID design principles

# Single Responsibility Principle: Every software entity should only have a single responsibility
# By separating the format and the content for the document.

# Open-closed Principle: Software entities should be open for extension but closed for modification
# The Formater class does not need to be modified to be extended.

# Liskov Substitution Principle: The aim of this principle is to ascertain that a sub-class can
# assume the place of its super-class without errors.

# Interface Segregation Principle: No client should be forced to depend on methods it does not use.
# Light weight abstract classes.

# Dependency Inversion: One should depend upon abstraction, not concretions
# By making HTMLDocumentFormater and WebPageHTMLDocumentFormater be dependent on the abstract classes.


class TextFormater:
    """
    Interface for text formating.
    """

    def format(self, text):
        raise NotImplementedError


class DocumentFormater:
    """
    Interface for document formating.
    """

    def format(self, document):
        raise NotImplementedError


class TagTextFormater(TextFormater):
    """
    Formats the text by tagging it on both sides.
    """

    def __init__(self, tag):
        """
        Constructor

        :param tag: Tag to format with
        :type tag: str
        """
        self._tag = tag

    def set_tag(self, tag):
        """
        Set tag to format text with.

        :param tag: Tag to format with
        :type tag: str
        """
        self._tag = tag

    def format(self, text):
        """
        Formats the text.

        :param text: Text to format
        :type text: str
        :return: Formated text
        :rtype: str
        """

        return '<{tag}>{text}</{tag}>'.format(tag=self._tag, text=text)


class HTMLDocumentFormater(DocumentFormater):
    """
    Formats the documents as HTML.
    """

    def __init__(self, title_formater, content_formater):
        """
        Constructor

        :param title_formater: Formater for title
        :type title_formater: TextFormater
        :param content_formater: Formater for content
        :type content_formater: TextFormater
        """
        self._title_formater = title_formater
        self._content_formater = content_formater

    def set_title_formater(self, title_formater):
        """
        Set title formater.

        :param title_formater: Formater for title
        :type title_formater: TextFormater
        """
        self._title_formater = title_formater

    def set_content_formater(self, content_formater):
        """
        Set content formater.

        :param content_formater: Formater for content
        :type content_formater: TextFormater
        """
        self._content_formater = content_formater

    @decorators.log_timing
    def format(self, document):
        """
        Formats the text as HTML text.

        :param document: The document to format
        :type document: Document
        :return: Formated the document as a HTML string
        :rtype: str
        """
        return '{title}<br>{content}'.format(
            title=self._title_formater.format(document.get_title()),
            content=self._content_formater.format(document.get_content())
        )


class WebPageHTMLDocumentFormater(HTMLDocumentFormater):
    """
    Formats the document as a HTML web page.
    """

    def __init__(self, header_text, *args):
        """
        Constructor

        :param header_text: Header text for the web page
        :type header_text: str
        :param args: Arguments requested by HTMLDocumentFormater
        """
        self._header_text = header_text
        super(WebPageHTMLDocumentFormater, self).__init__(*args)

    @decorators.log_timing
    def format(self, document):
        """
        Formats the text as HTML web page.

        :param document: The document to format
        :type document: Document
        :return: Formated the document as a HTML string
        :rtype: str
        """
        return '<head>{header}</head><body>{document}</body>'.format(
            header=self._header_text,
            document=super().format(document)
        )











