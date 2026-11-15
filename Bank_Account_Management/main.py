import random
import os

class Users:

    def __init__(self, name):
        self.name = name
        num = random.randint(1000, 9999)
        self.acc_no = "500070" + str(num)
        self.balance = 0

    def show_details(self):
        details = (f"name: {self.name}\n"
        f"account number: {self.acc_no}\n"
        f"balance: {self.balance}")
        return details


# Create object
# user_1 = Users(input("Enter your name: "))

# Display details
# print(user_1.show_details())

# main loop
while True:
    print("****main menu****")
    print("1.Create new account")

    choice = int(input("enter your choice: "))
    if choice == 1:
        # code to create a new account
        name = input("enter your name: ")
        folder_path = "C:\\Users\\suman\\OneDrive\\Desktop\\my_codes\\git_clones\\Mini_Projects\\Bank_Account_Management\\users"
        def creating_user_id():
            user_id = random.randint(1000,9999)
            file_path = os.path.join(folder_path, str(user_id) + ".txt")
            if os.path.isfile(file_path):
                creating_user_id()
            else:
                with open(file_path,"w") as f1:
                    f1.write(f"WELCOME {name}")

            return user_id
        acc_id = creating_user_id()
        print(acc_id)
        break
            

    else:
        print("Incorrect Entry!")
        break