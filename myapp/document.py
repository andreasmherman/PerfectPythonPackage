class Document:
    """
    Encapsulation of document data.
    """

    def __init__(self, title, content):
        """
        Constructor

        :param title: Title for the document
        :type title: str
        :param content: Content for the document
        :type content: str
        """
        self._title = title
        self._content = content

    def set_title(self, title):
        """
        Set title.

        :param title: Title for the document
        :type title: str
        """
        self._title = title

    def set_content(self, content):
        """
        Set content.

        :param content: Content for the document
        :type content: str
        """
        self._content = content

    def get_title(self):
        """
        Get title.

        :return: Title for the document
        :rtype: str
        """

        return self._title

    def get_content(self):
        """
        Get content.

        :return: Content for the document
        :rtype: str
        """
        return self._content