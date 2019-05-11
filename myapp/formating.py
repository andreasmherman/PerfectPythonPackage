# -*- coding: utf-8 -*-

from . import decorators

# Single Responsibility Principle by separating the format and the content for the document.

# Open-closed Principle when the Formater class does not need to be modified to be extended.

# Dependency Inversion by making HTMLDocumentFormater and WebPageHTMLDocumentFormater be dependent on the abstract
# TextForamter and DocumentFormater. Liskov Substitution Principle.

# Interface Segregation Principle by forcing classes depend on methods they do not use.


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

    def __init__(self, header_text, **kwargs):
        """
        Constructor

        :param header_text: Header text for the web page
        :type header_text: str
        :param kwargs: Arguments requested by HTMLDocumentFormater
        """
        self._header_text = header_text
        super().__init__(**kwargs)

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











