#!/usr/bin/env python3

# simple contancts function uses a dictionary (dict) data structure
# the information about some contacts is managed as (key, value) pair
# in this example, the key is associated to the person name and
# the value to his/her phone number
def simple_contacts():
    # here, an empty dict
    contacts = {}
    
    # use the form dict[key] = value to insert new items
    contacts["Farah"] = "417-6845"
    contacts["Dave"] = "578-8073"
    contacts["Greta"] = "922-3642"
    contacts["Bob"] = "950-9528"
    contacts["Anne"] = "701-6708"
    contacts["Carl"] = "181-8903"
    contacts["Emma"] ="248-3494"
    
    # you can use the function len() to obtain the dimension of the dictionary
    print("In my contacts book I have {} people".format(len(contacts)))
    
    # dict provides the function keys(), which returns the list of keys
    # i.e., the names of my contacts
    print("I know the following people:", contacts.keys())
    
    # as mentioned before, the dict stores (key, value) pairs
    # to access them, you have to use items() function provided by dict
    for person, phone in contacts.items():
        print("{}'s phone number is {}".format(person, phone))
    
    # to access a value assocated to a key, use the form dict[key]
    print("Do I have Beatrice's phone number?", contacts["Beatrice"])
    print("Do I have Farah's phone number?", contacts["Farah"])
    
    # to update an item's value, just use the form dict[key] = newvalue
    contacts["Anne"] = "655-7783"
    print("Anne has changed her phone number, the new one is", contacts["Anne"])
    

simple_contacts()
