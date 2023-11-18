#Contact List Manager: Create a 
#program that allows users to 
#manage a contact list using OOP 
#concepts. This program should 
#enable users to create, edit, and 
#delete contacts. It should also 
#provide functionality to search 
#for a particular contact and 
#display all contacts.

#Contact organization: Contact 
#list managers allow users to 
#categorize their contacts into
# groups, such as friends, family,
# colleagues, or customers. This 
#makes it easy to find and 
#communicate with specific groups 
#of people.




def tel_no_check(num):
        check = False if len(num) < 10 or len(num) > 10 else True
        return True
        
        
def create_contact():
            name = input('Name: ')               
            number = input('Number: ')
            if not tel_no_check(number):
                print('Invalid')
                while  not tel_no_check(number):
                    number = input('Number: ')
                return (name, number)
            else:
                return (name, number)
            




class Contact:

    contacts = []  
    
    def __init__(self, name, number):
        assert len(number) == 10, f"Phone number '{number}' is not made up of 10 digits"
        self.name = name
        self.number = number
        Contact.contacts.append(self)
        li = Contact.contacts
        
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name} <==> {self.number})"
        
        
    @staticmethod
    def show_contact():    
        for instance in Contact.contacts:
            print(f'''
Name:  {instance.name}
Phone Number: {instance.number}
''')
    @staticmethod
    def search_contact():
        search = input('Enter name of search 🔍: ')
        for instance in Contact.contacts:
            if search == instance.name:             
                return search, instance.number, True
                break
            else:
                print('Search Not Found...')
                
            
            
    @classmethod
    def replace(cls, Contact.contacts, item, replacement):      
        for instance in Contact.contacts:
            if self.name == item:
                z = Contact.contacts.index(instance)
                Contact.contacts[z] = replacement 
        print(Contact.contacts)       
        
        
             
    @classmethod
    def edit_contact(cls):
        a, b, c = self.search_contact()
      
        action = input('Are you editting the name or the number?  ').lower()
        if action == "name":
            new_name = input('The New Name: ')            
            e = f"{self.__class__.__name__}({new_name} <==> {b})"
            d = f"{self.__class__.__name__}({a} <==> {b})"
            
            self.replace(self.li,d, e)
            #print(Contact.contacts)
            
        elif action == "number":
            new_number = input('The New Number: ')  
             
            if len(new_number) != 10:         
                print('Error: Invalid Number')
            
                while len(new_number) != 10 :
                   new_number = input('The New Number: ')
                   if len(new_number) == 10:
                       self.number = new_number
                       break
                   else:
                       continue 
                print(a, self.number)
            
            else:
                self.number = new_number
                print(a, self.number)
        else:
            print('Invalid action')
#name, number = create_contact()

x = Contact("Bennis", "0568756123")
y = Contact("Dan", "0242852661")
z = Contact("Randy", "0242555661")
m = Contact("Truddy", "0592555661")
#print (Contact.show_contact())

Contact.edit_contact()




    
     