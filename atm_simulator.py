#ATM Simulator

class Atm:
    def __init__(self,account_holder,pin_num):
        self.account_holder_name=account_holder
        self.pin_number=pin_num
        self.balance=0

    def check_balance(self,entered_pin):
        if entered_pin==self.pin_number:
            print(f"Dear {self.account_holder_name}.Your Account balance is {self.balance}")
        else:
            print("Incorrect PIN.Try again")

    def deposit(self,amount,entered_pin):
        if entered_pin == self.pin_number:
            self.balance+=amount
            print(f"Successfully deposited amount {amount}.\nNew balance is {self.balance}")
        else:
            print("Incorrect PIN.Try again!!")

    def withdraw(self,amount,entered_pin):
        if entered_pin == self.pin_number:
            if amount<=self.balance:
                self.balance-=amount
                print(f"Successfully withdrawn amount {amount}.\nCurrent balance is {self.balance}")
            else:
                print(f"No sufficient balance.Your balance is {self.balance}")
        else:
            print("Incorrect PIN.Try again!!")

    def change_pin(self,old_pin,new_pin,confirm_pin):
        if old_pin == self.pin_number:
            if new_pin==confirm_pin:
                self.pin_number=new_pin
                print("PIN changed successfully.")
            else:
                print("New PIN and Confirmation PIN do not match\n.Please try again.")
        else:
            print("Incorrect old PIN.Enter your correct PIN number:")

print()
print('"'*50)
print("       Dear Customer, Welcome to ABC Bank")
print('"'*50)

account_name=input("Enter Account holder name:")
account_pin=int(input("Enter your PIN number:"))
print("_" * 50)
my_atm=Atm(account_name,account_pin)

#--------------------------main program-------------------------------------------------

while True:

    print("\n           PLEASE SELECT A SERVICE")
    print("_" * 50)

    print("1.Balance Enquiry")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Change Pin")
    print("5.Exit")
    print("_" * 50)

    choice=int(input("Enter your choice (1-5):"))
    print("-" * 50)

    if choice==1:
        print(" "*15,"BALANCE HERE...\n")
        input_pin=int(input("Enter your PIN number:"))
        my_atm.check_balance(input_pin)
        print("-"*50)
    elif choice==2:
        print(" "*15,"DEPOSIT HERE...\n")
        input_pin=int(input("Enter your PIN number:"))
        deposit_amount=int(input("Enter your amount:"))
        my_atm.deposit(deposit_amount,input_pin)
        print("-" * 50)
    elif choice==3:
        print(" "*15,"WITHDRAW HERE...\n")
        input_pin = int(input("Enter your PIN number:"))
        withdraw_amount = float(input("Enter your amount:"))
        my_atm.withdraw(withdraw_amount,input_pin)
        print("-" * 50)

    elif choice==4:
        print(" "*15,"CHANGE PIN HERE...\n")
        input_old_pin = int(input("Enter your old PIN number:"))
        input_new_pin = int(input("Enter Your new Pin : "))
        input_confirm_pin = int(input("Enter Your confirmation Pin : "))
        my_atm.change_pin(input_old_pin,input_new_pin,input_confirm_pin)
        print("-" * 50)

    elif choice==5:
        print("        THANK YOU FOR USING THIS SERVICE")
        print("-" * 50)
        break
    else:
        print("Invalid choice.please select valid choice")


















