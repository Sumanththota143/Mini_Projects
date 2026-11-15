import random
import os

class users:
    def __init__(self, name, account_id, password, balance):
        self.name = name
        self.account_id = account_id
        self.password = password
        self.balance = balance
        folder_path = "C:\\Users\\suman\\OneDrive\\Desktop\\my_codes\\git_clones\\Mini_Projects\\Bank_Account_Management\\users"
        file_path = os.path.join(folder_path, str(self.account_id) + ".txt")
        with open(file_path,"w") as f2:
            f2.write(f"name: {self.name}\n")
            f2.write(f"account id: {self.account_id}\n")
            f2.write(f"password: {self.password}\n")
            f2.write(f"balance: {self.balance}\n")



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
        account_id = creating_user_id()
        print("your account id is: ",account_id)
        def creating_pin():
            pin = int(input("create your pin: "))
            pin_check = int(input("re enter your pin: "))
            if pin != pin_check:
                print("password dosent match..\n")
                creating_pin()
            else:
                return pin
        password = creating_pin()
        balance = 0

        user = users(name,account_id,password,balance)
        break
    else:
        print("Incorrect Entry!")
        break
