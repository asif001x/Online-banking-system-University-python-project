print('''Welcome TO Shomobaey Puji E-Banking''')
print("\n")
#                [Id, Name , Amount, Password]
Details = [["2110384", "Md Asifur Rahman", 14000, "1234"], ["2210652", "Sunjidur Rahman", 12000, "1234"], ["2210653", "Md Firoj", 10000, "1234"],
              ["2110387", "Kabbo", 11000, "1234"], ["2110388", "Moni", 5000, "1234"]]
def Open_New_account():
    print("**** Enter New Account details ****")
    Iub_ID = input("Your Iub Id: ")
    for i in range(len(Details)):
        if Iub_ID==Details[i][0]:
            print("This Id Already Use For Open Account.")
            break
        else:
            name = input("Your full Name: ")
            Amount = float(input("Enter your Despite amount price: "))
            pass_ = input("Enter your Four Digit Password: ")
            New_Id = [Iub_ID, name, Amount, pass_]
            Details.append(New_Id)
            print("\n")
            print(f'New Account Open \nName:{name} \nMembership Id:{Iub_ID}.')
        break
def Depsite_money():
    Iub_ID = input("Your Membership/Iub Id : ")
    name = input("Your Full Name: ")
    Month = int(input("How Money Month Would You Give(Per Month 2000/-): "))
    for i in range(len(Details)):
        if Iub_ID == Details[i][0]:
            Details[i][2] = Details[i][2]+(Month*2000)
            print(f'Your Money Despite Successfully \nYour New Balance is {Details[i][2]} Taka')
            break
        else:
            print("No Account Open In This Membership/Iub Id.")
        break

def withdrow_money():
    Iub_ID = input("Your Membership/Iub Id: ")
    pass_ = input("Enter Your Password: ")
    for i in range(len(Details)):
      if Iub_ID == Details[i][0] and pass_ == Details[i][3]:
          if Details[i][2]>=12000:
              withdrow = int(input("How Much Money You Want To Withdraw :"))
              if withdrow <= Details[i][2]:
                  print(f'Withdraw {withdrow} Taka Successfully.')
                  Details[i][2]=Details[i][2]-withdrow
                  print(f'Your New Balance Is {Details[i][2]} Taka.')
              else:
                  print("Insufficient Balance.")
          else:
              print(f"Your Current Balance is {Details[i][2]} For Withdraw You Have Maintain At Least 12000 Taka.")
              break
          break

      else:
          print(f'Incorrect Id or Password. \nTry Again.')
      break

def personal_account_details():
    Iub_ID = input("Your Membership/Iub Id :")
    pass_ = input("Enter Your Password :")
    for i in range(len(Details)):
       if Iub_ID == Details[i][0] and pass_ == Details[i][3]:
          print(f'Name:{Details[i][1]}  Account Balance:{Details[i][2]}')
          break
       else:
          print(f'Incorrect Id or Password. \nTry Again.')
       break


def close_your_account():
    Iub_ID = input("Your Membership/Iub Id :")
    pass_ = input("Enter Your Password :")
    for i in range(len(Details)):
        if Iub_ID == Details[i][0] and pass_ == Details[i][3]:
            Details.pop(i)
            break
        else:
            print(f'For Close your Account Give Correct Id And Password.')
        break
def change_password():
    Iub_ID = input("Your Membership/Iub Id: ")
    pass_ = input("Enter Your Password: ")
    for i in range(len(Details)):
        if Iub_ID == Details[i][0] and pass_ == Details[i][3]:
            new_pass=input("Enter Your New Four Digit Password: ")
            Details[i][3]=new_pass
            print("Change Password Successfully.")
            break
        else:
            print(f'For Change Password Give Correct Information.')
        break

option = 10
while option != "0":
    print("What do you wish to do?")
    print("1 -> Open new account")
    print("2 -> Despite money")
    print("3 -> Personal Account Details")
    print("4 -> Withdraw Money")
    print("5 -> Change Old Password")
    print("6 -> Close Your Account")
    print("0 -> Exit menu")
    option = input("Select option: ")
    print("\n")  #
    if option == "1":
        Open_New_account()
        print("\n")

    elif option == "2":
        Depsite_money()
        print("\n")

    elif option == "3":
        personal_account_details()
        print("\n")

    elif option == "4":
        withdrow_money()
        print("\n")

    elif option == "5":
        change_password()
        print("\n")

    elif option == "6":
        close_your_account()
        print("\n")


