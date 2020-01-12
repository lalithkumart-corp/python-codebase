class TuplesDict:
    def handle(self):
        '''
        PYTHON FOR DATA SCIENCE - TUPLES AND DICTIONARY
        '''

        # define a tuple
        my_tuple = (1, 2, 3, 4, 5)

        # access single element using index
        print('TUPLE = ',my_tuple)

        print('\n\nelement at index 1 = ',my_tuple[1])

        # uncomment the below code and you see the error as the tuples are immutable
        #my_tuple[2] = 4

        # define a dictionary
        my_dict = {
        'key_1' : 4,
        'key_2' : 5,
        'key_3' : 6,
        'key_4' : 7
        }

        # access value of any key
        print('\n\nThe value of key_1 in the dictionary is ',my_dict['key_1'])

        # dictionaries are mutable
        my_dict['key_1'] = 1000

        print('\n\nThe value of key_1 after update in the dictionary is ',my_dict['key_1'])


        #keys of dictionary
        print('\n\nkeys = ',my_dict.keys())        