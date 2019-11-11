
class BcEncode:
    '''
    This class is used to encode a text based on a book given.
    the encode should then return a enciphered text that holds
    all the information from the text but in a line
    '''

    def __init__(self, book, text):
        self.__text = text
        self.__book = book
        self.__struct_ord = []


    def encode(self):
        '''
        PSEUDO CODE:
        create a acsii list
        read book file and parse the chars into lists of corrdinate pairs that apply to ord()

        '''
        for i in range(0, 255):
            __struct_ord = [ord(i)]
