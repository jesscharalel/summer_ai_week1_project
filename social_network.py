# # #Various import Statements can go here
# # def edit_profile():
# #     return input("Edit Your Profile Details: ")

# # def edit_bio():
# #     return input("Edit Your Bio Details: ")

# from  social_network_classes import SocialNetwork,Person
# from social_network_classes import SocialNetwork
# import social_network_ui


# def mainMenu():
#     print("")
#     print("1. Create a new account")
#     print("2. Manage my account")
#     print("3. Quit")
#     print("********************************************************")
#     return input("Please Choose a number: ")

# def manageAccountMenu():
#     print("1. Edit my details")
#     print("2. Add a friend")
#     print("3. View all my friends")
#     print("4. View all my messages")
#     print("5. <- Go back ")
#     return input("Please Choose a number: ")
#     # choice = social_network_ui.manageAccountMenu 
#     # if choice == "1":
#     #         print("1. Edit Profile")
#     #         print("2. Edit Bio")
            
#     #         if choice =="1":
#     #             print("\nOpen Edit Profile")
#     #         ai_social_network.edit_profile
            
#     #         if choice =="2":
#     #             print("\nOpen Edit Bio")
#     #         ai_social_network.edit_bio




# #Create instance of main social network object
# ai_social_network = SocialNetwork()

# #The line below is a python keyword to specify which 
# if __name__ == "__main__":
#     print("########################################################")
#     print("          Welcome to Summer AI Social Network")
#     print("########################################################")
#     last_menu = None
#     choice = social_network_ui.mainMenu()

#     while True: 
#         if choice == "1":
#             print("\nYou are now in the create account menu")
#             ai_social_network.create_account()

#         elif choice == "2":
#             inner_menu_choice = social_network_ui.manageAccountMenu()
#             #Handle inner menu here
#             while True:
#                 if inner_menu_choice == "5":
#                     break
#                 else:
#                     inner_menu_choice = social_network_ui.manageAccountMenu()

#         elif choice == "3":
#             print("Thank you for visiting. Goodbye3")
#             break

#         else:
#             print("Your input is invalid. Try Again!")
        
#         #restart menu
#         choice = social_network_ui.mainMenu()


# choice = social_network_ui.manageAccountMenu 
# if choice == "1":
#             print("1. Edit Profile")
#             print("2. Edit Bio")
            
#             if choice =="1":
#                 print("\nOpen Edit Profile")
#             social_network_ui.edit_profile
            
#             if choice =="2":
#                 print("\nOpen Edit Bio")
#             social_network_ui.edit_bio
from  social_network_classes import SocialNetwork,Person
import social_network_ui



def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. View all my messages")
    print("5. Block a friend")
    print("6. <- Go back ")
    return input("Please Choose a number: ")


#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()

        elif choice == "2":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            
            active_user=None
            user_choice=input("Enter the name of the account you want to manage: ")
            
            #Handle inner menu here
            while True:
            
                for user in ai_social_network.list_of_people:
                    if user.id==user_choice:
                        active_user=user
                if inner_menu_choice=="1":
                    active_user.edit_details()
                    
                elif inner_menu_choice=="2":
                    print("Enter the name of friend: ")
                    new_friend=input()
                    for friend in ai_social_network.list_of_people:
                    
                        if friend.id==new_friend:
                            new_person=friend
                            active_user.add_friend(new_person)
                        
                             
                        
                    
                elif inner_menu_choice=="3": 
                    active_user.view_friendlist() 

                if inner_menu_choice == "5": 
                    print("Enter the name of the friend: ")
                    blocked_friend=input()
                    for friend in ai_social_network.list_of_people:
                    
                        if friend.id==blocked_friend:
                    
                            active_user.block_friend(friend)
                
                if inner_menu_choice == "6":
                    break
            
                #else:
                    #print("Invalid choice") 
                inner_menu_choice = social_network_ui.manageAccountMenu()   
                    
        elif choice == "3":
            print("Thank you for visiting. Goodbye")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()


      
