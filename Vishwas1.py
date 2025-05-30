import random
import time
now = time.ctime()
cust_otp = {8183838838: 345789,7090076326: 678345,9902750970: 543098,9901505558: 987123,8722260887: 907435}
cust_name = {8183838838: 'Srinivas Rao B',7090076326: 'V Sai Kishore',9902750970: 'Shree Darshan M',9901505558: 'Vinay Kumar',8722260887: 'Vishwas S S'}
cust_bal = {8183838838: 25000,7090076326: 30000,9902750970: 42000,9901505558: 5000,8722260887: 100}
cust_acc_type = { 8183838838: 1, 7090076326: 3, 9902750970: 2, 9901505558: 3,8722260887: 1}
cust_pin = {8183838838: 2827,7090076326: 4567,9902750970: 9005,9901505558: 3489,8722260887: 2119}
cust_ac_no={8183838838:40400609771,7090076326:40061234990,9902750970:60904400056,9901505558:48700098720,8722260887:6008731109}

def get_user_info(user_input):
    return user_input in cust_name

def get_password(entered_otp, user_input):
    return entered_otp == str(cust_otp.get(user_input))

def print_receipt(ch):
    print()
    print("Transaction Successful")
    print()
    print("-------------------- RECEIPT --------------------------")
    print("XYZ Bank           ", now)
    print("------------------------------------------------------------")
    print("Customer Name:    ",cust_name.get(user_input))
    print("Account Number:   ",cust_ac_no.get(user_input))
    print("Customer Card :      xxxx xxxx xxxx", random.randint(1000, 9999))

    if ch==1:
        print("Transaction:            Withdraw")
        print("Amount:                  ₹", amt)
    elif ch==2:
        print("Transaction:            Balance Enquiry")
    elif choice==3:
        print("Transaction:            Deposit")
        print("Amount:                 ₹", amt1)
    print("Available Balance:   ₹", cust_bal[user_input])
    print("ATM Charges:         ₹0.0")
    print("--------------------------------------------------------")
    print("Thank you for using our ATM\n")
    
while True:
    print("================================================================================")
    print("Welcome to Cardless Transaction")
    user_input = int(input("Enter your Phone Number linked to Bank: "))

    if get_user_info(user_input):
        print("Welcome", cust_name[user_input])

        otp = random.randint(100000, 999999)
        cust_otp[user_input] = otp
        print()
        print("OTP sent to your phone:", otp)
        print()
        user_otp = input("Enter OTP: ")
    
        if get_password(user_otp, user_input):
            print()
            print("Select Transaction")
            print("1. Cash Withdrawal")
            print("2. Balance Enquiry")
            print("3. Cash Deposit")
            print("4. Exit")
            print()
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print()
                print("Select Account type")
                print("1. Savings")
                print("2. Current")
                print("3. Business")
                print()
                acc_type_input = int(input("Enter your Account Type: "))
                if acc_type_input == cust_acc_type[user_input]:
                    pin = int(input("Enter PIN: "))
                    if pin == cust_pin[user_input]:
                        amt = int(input("Enter amount to withdraw: ₹"))
                        if amt <= cust_bal[user_input]:
                            cust_bal[user_input] -= amt
                            print("Withdraw Successful")
                            print("Your updated balance is: ₹", cust_bal[user_input])
                            print_receipt(1)
                        else:
                            print("Insufficient balance")
                            print("Last Transaction Cancelled")
                    else:
                        print("Invalid PIN")
                        print("Last Transaction Cancelled")
                        
                else:
                    print("Invalid Account Type")
                    print("Last Transaction Cancelled")
                   

            elif choice == 2:
                print()
                print("Select Account type")
                print("1. Savings")
                print("2. Current")
                print("3. Business")
                print()
                acc_type_input = int(input("Enter your Account Type: "))
                if acc_type_input == cust_acc_type[user_input]:
                    pin = int(input("Enter PIN: "))
                    if pin == cust_pin[user_input]:
                        print("Your current balance is: ₹", cust_bal[user_input])
                        print_receipt(2)
                    else:
                        print("Invalid PIN")
                        print("Last Transaction Cancelled")
                            
                else:
                    print("Invalid Account Type")
                    print("Last Transaction Cancelled")
                        

            elif choice == 3:
                print()
                print("Select Account type")
                print("1. Savings")
                print("2. Current")
                print("3. Business")
                print()
                acc_type_input = int(input("Enter your Account Type: "))
                if acc_type_input == cust_acc_type[user_input]:
                    pin = int(input("Enter PIN: "))
                    if pin == cust_pin[user_input]:
                         amt1 = int(input("Enter amount to Deposit(MAX 20,000): ₹"))
                         if amt1<= 20000:
                                cust_bal[user_input] += amt1
                                print("Deposit Successful")
                                print("Your updated balance is: ₹", cust_bal[user_input])
                                print_receipt(3)
                         else:
                            print("Try Smaller amount")
                            print("Last Transaction Cancelled")
                    else:
                        print("Invalid PIN")
                        print("Last Transaction Cancelled")
                            
                else:
                    print("Invalid Account Type")
                    print("Last Transaction Cancelled")

            elif choice == 4:
                print("Thank you for using our ATM. Goodbye!")
                

            else:
                print("Invalid choice")
                print("Last Transaction Cancelled")
                

        else:
            print("Incorrect OTP. Try again.")
            print("Last Transaction Cancelled")
            
    else:
        print("User Not Found")
        print("Last Transaction Cancelled")
        
