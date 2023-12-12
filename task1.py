import hashlib
import csv
def Register(username,passcode):
    hashed_passcode=hashlib.sha256(passcode.encode()).hexdigest()
    with open("user_details.csv",mode="a",newline="") as file:
        write=csv.writer(file)
        write.writerow([username,hashed_passcode])
    print("Registration Successful")

def login(username,passcode):
    hashed_passcode=hashlib.sha256(passcode.encode()).hexdigest()
    with open("user_details.csv",mode="r") as file:
        read=csv.reader(file)
        for row in read:
            if row[0]==username and row[1]==hashed_passcode:
                print("login successful")
                return True
    print("Login failed,invalid username or passcode")
    return False
def main():
    while True:
        print("\n1.Register")
        print("2.Login")
        option=input("Select an option:1/2=")

        if option=="1":
            print("Enter your registration details :")
            username=input("Enter your username =")
            passcode=input("Enter your passcode =")
            Register(username,passcode)

        elif option=="2":
            print("Enter your login details :\n")
            username=input("Enter your username =")
            passcode=input("Enter your passcode =")
            login(username,passcode)

        else:
            print("Error, Please enter correct choice 1/2")
main()



