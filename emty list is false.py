purchase_amounts = []
subtotal = 0
total = 0

while True:
    usr = input("Enter a purchase amount. ")
    if usr.lower() == "done":
        break
    else: usr = int(usr)
    purchase_amounts.append(usr)
    total += usr


while purchase_amounts:
    last_item = purchase_amounts.pop()
    subtotal += last_item

print(subtotal)
print(total)
    
