print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").upper()
bill = 0
if size == "S":
    bill+=15
elif size =="M":
    bill+=20
elif size =="L":
    bill+=25
else:
    print("invalid size")

pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
if pepperoni == "Y" and size == "S":
    bill+=2
elif pepperoni == "Y" and size == "M":
    bill+=3
elif pepperoni == "Y" and size == "L":
    bill+=4
elif pepperoni == "N":
    print(f"your final bill is $:{bill}")

extra_cheese = input("Do you want extra cheese? Y or N: ").upper()
if extra_cheese == "Y":
    bill+=3
    print(f"your final_bill is $:{bill}")
else:
    print(f"your final_bill is $:{bill}")