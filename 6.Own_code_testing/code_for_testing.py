from abc import ABC, abstractmethod


class ArtMuseum(ABC):
    def __init__(self, name: str = None, creation_year: int = None, author: str = None, for_sale: bool = True):
        self.__name = name
        self.__creationYear = creation_year
        self.__author = author
        self.__sale = for_sale

    @abstractmethod
    def brief_overview(self, overview: str):
        """The overview of the artwork will be here"""

    @property
    def name(self):
        return '\nName: ' + self.__name

    @property
    def creation_year(self):
        return '\nYear of creation: ' + str(self.__creationYear)

    @property
    def author(self):
        return '\nAuthor: ' + self.__author

    @property
    def sale(self):
        if self.__sale:
            return '\nSale status: for sale'
        return '\nSale status: not for sale'

    @name.setter
    def name(self, value):
        self.__name = value

    @creation_year.setter
    def creation_year(self, value):
        self.__creationYear = value

    @author.setter
    def author(self, value):
        self.__author = value

    @sale.setter
    def sale(self, value):
        self.__sale = value

    def change_sale_status(self, new_status: bool):
        self.__sale = new_status


class Pictures(ArtMuseum):
    def brief_overview(self, overview: str):
        pic_overview = overview
        return '\nPicture overview: ' + pic_overview

    def __category_description(self):
        return 'A category contains information about pictures of the museum'

    def __access_to_changes(self):
        return 'Only an administrator can adjust the "Pictures category"'

    def info_for_qa(self):
        return '\n\nMemo for QA:\n' + self.__category_description() + '\n' + self.__access_to_changes() + \
               '\n' + 'Just test the "Pictures category"!'


class Sculptures(ArtMuseum):
    def brief_overview(self, overview: str):
        sculp_overview = overview
        return '\nSculpture overview: ' + sculp_overview

    def __category_description(self):
        return 'A category contains information about sculptures of the museum'

    def __access_to_changes(self):
        return 'Only an administrator can adjust the "Sculptures category"'

    def info_for_qa(self):
        return '\n\nMemo for QA:\n' + self.__category_description() + '\n' + self.__access_to_changes() + \
               '\n' + 'Just test the "Sculptures category"!'