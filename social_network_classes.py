# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
    
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def  create_account(self):
        #implement function that creates account here
        print("Creating ...")
        age=input("Type age: ") 
        name=input("Type name: ")
        created_account=Person (name,age)

        self.list_of_people.append(created_account)

        print(self.list_of_people)
class Person:
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []
    def edit_details(self):
        new_name=print("Enter new name: ")
        new_age=print("Enter new age: ")
        self.id=new_name
        self.year=new_age

    def add_friend(self, person_object):
        self.friendlist.append(person_object)
        #implement adding friend. Hint add to self.friendlist
       
    def block_friend(self, person_object):
        self.friendlist.remove(person_object)

    def view_friendlist(self):
        for friend in self.friendlist: 
            print(friend.id)

    def send_message(self):
        #implement sending message to friend here
        pass
