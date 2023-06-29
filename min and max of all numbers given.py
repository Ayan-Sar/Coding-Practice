mn = float('inf') 
mx = 0 
a = input("Enter a number: ") 
while a != 'done': 
    try: 
        a = int(a) 
        # If a is smaller than mn, a is minimum 
        if a < mn: 
            mn = a 
        # If a is bigger than mx, a is maximum 
        if a > mx: 
            mx = a 
    except: 
        print("Invalid input") 
    a = input("Enter a number or 'done' to stop entering numbers: ") 
 
print("Minimum:", mn, "\nMaximum:", mx) 