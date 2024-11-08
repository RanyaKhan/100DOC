print("welcome to the tip calculator!")
bill= input("what was the total bill? ")
percent= input("how much top would you like to give 10, 12 or 15? ")
split= input("how many people to split the bill? ")

total= (int(bill)*(1+int(percent)/100))/int(split)
print(f"each person should pay: {total}")