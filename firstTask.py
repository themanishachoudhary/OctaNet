import time

print("Please insert your CARD")

time.sleep(2) #for taking 2 seconds of time for showing the information.

password=1234

pin=int(input("Enter your ATM pin : "))

balance = 5000

if pin==password:
    while True:
    
        print("""
            1 == balance 
            2 == withdraw balance
            3 == deposit balance
            4 == exit
            """)
        # interface of ATM
        try:
            option = int(input("*****Please enter your choice***** : "))
        except:
            print("Please enter valid option")

        if option == 1:
            print(f"Your current balance is {balance}")

        if option == 2:

            withdraw_amount=int(input("Please enter withdraw_amount : "))

            balance = balance - withdraw_amount

            print(f"{withdraw_amount} is debited from your account")

            print(f"Your updated balance is : {balance}")
        
        if option == 3:

            deposit_amount = int(input("Please enter deposit_amountn : "))

            balance = balance+deposit_amount
            
            print(f"{deposit_amount} is credited to your account")

            print(f"Your updated balance is : {balance}")

        if option==4:

            print("Thank You")
            break


else:
    print("Wrong pin please try again.")