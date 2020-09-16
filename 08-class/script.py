#!/usr/bin/env python3

# this script uses the concepts explained in 05-dict
# by using a class as a "value" field within a dict

# a way to represent more information about a contact
# is to use a Class, like in C++ and Java
class Contact:
    
    # __init__ is the constructor of the class
    # like C++ or Java, it creates a new object of the class
    # by simply using the form Contact()
    def __init__(self, name, phone):
        
        # the following are the fields of the class
        # this is an admissible way to declare them
        
        # notice that some fields are required as parameters to the constructor
        self.name = name
        self.phone = phone
        
        # instead these are not important, so they can be initialized to None (empty field)
        self.address = None
        self.email = None
        self.office = None
        self.wesite = None
    
    # this method is invoked when str() is used over a Contact instance
    def __str__(self):
        return "\nName: {}\nPhone: {}\nAddress: {}\nEmail: {}\nOffice: {}\nWebsite: {}\n".format(self.name, self.phone, self.address, self.email, self.office, self.website)


# use advanced_contacts if you want to play with the class and its objects
def advanced_contacts():
    contacts = {}
    contacts["Anne"] = Contact("Anne", "655-7783")
    
    # if you miss a field of the class, you can use None to fill it
    contacts["Beatrice"] = Contact("Beatrice", None)
    
    contacts["Carl"] = Contact("Carl", "181-8903")
    contacts["Dave"] = Contact("Dave", "578-8073")
    contacts["Emma"] = Contact("Emma", "248-3494")
    contacts["Farah"] = Contact("Farah", "417-6845")
    contacts["Greta"] = Contact("Greta", "922-3642")
    
    # dict.get(key) is an alternative way to access elements
    
    # because dict's values have "datatype" Contact
    # you can access the fields of Contacts after using dict.get
    # and perform some updates directly into the dictionary
    contacts.get("Beatrice").email = "supplychain@biz.com"
    contacts.get("Beatrice").website = "https://biz.com/customers"
    contacts.get("Carl").office = "69050, Kennedy St., B-205"
    contacts.get("Dave").office = "69050, Kennedy St., B-206"
    contacts.get("Anne").address = "2114, Wisconsin St."
    contacts.get("Emma").address = "2114, Wisconsin St."
    contacts.get("Farah").email = "farah.day@mail.com"
    
    # dict.values() returns the list of values
    for contact in contacts.values():
        # we are using str() over a Contact instance
        print(str(contact))
    
    # with dict.get() you can specify an alternative value
    # e.g., the used key has no value associated so use a "default" one
    print("Do I have Sarah's contact?", contacts.get("Sarah", "No"))
    

advanced_contacts()
 
