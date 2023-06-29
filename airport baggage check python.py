def check_baggage(baggage_weight):
    if baggage_weight > 0 and baggage_weight < 40:
        print ("True")
        return check_baggage == "True"
    else:
        print("False")
def check_immigration(expiry_date):
    if expiry_date >= 2030 and expiry_date <=2050:
        print("True")
        return check_immigration == "True"
    else:
        print("False")
def noc_status(m):
    if m == "valid":
        print("True")
        return noc_status == "True"
    else:
        print("False")
def traveller():
    baggage_weight = int(input("Enter your baggage weight in kilograms: "))
    expiry_date = int(input("Enter the expiry date of your passport: "))
    noc_status22 = input("Specify if your noc status is valid or invalid: ")
    check_baggage(baggage_weight)
    check_immigration(expiry_date)
    noc_status(noc_status22)
    if (check_baggage == "True" and check_immigration == "True" and noc_status == "valid"):
        print("Allow traveller to fly.Have a happy journey!!")
    else:
        print("Detain traveller for re-checking")
print("Hello everyone. Welcome to UPES Airlines. I'd like to check your credentials before we move forward towards your journey!!!")
name=input("Enter your name:")
ID=input("ID number:")
traveller()