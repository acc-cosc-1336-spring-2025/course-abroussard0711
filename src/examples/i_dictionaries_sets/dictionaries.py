def test_config():
    return True

def create_dictionary ():
    phone_book = {'Chris':'999-7773', 'David':'555-2226'}

    print (phone_book)

def dictionary_items ():
    phone_book = {'Chris':'999-7773', 'David':'555-2226', 'Sam':'888-2221'}

    for key, value in phone_book.items ():
        print (key, value)

def dictionary_keys ():
    phone_book = {'Chris':'999-7773', 'David':'555-2226', 'Sam':'888-2221'}

    for key in phone_book.keys ():
        print (key)

def dictionary_values ():
    phone_book = {'Chris':'999-7773', 'David':'555-2226', 'Sam':'888-2221'}

    for value in phone_book.values ():
        print (value)