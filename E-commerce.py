product=input("enter a product")
def products(price,quantity):
    return price*quantity
def discount(total):
    if total>=5000:
        return total*0.10
    elif total>=10000:
        return total*0.20
    else:
        return 0
def GST(amount):
    return amount*0.18
def delivery(total):
    if total>=1000:
        return 0
    else:
        return 100
price=int(input("Enter a price:"))
quantity=int(input("Enter a quantity:"))
delivery=int(input("Enter a delivery:"))
total=products(price,quantity)
discount_amount=discount(total)
GST_amount=GST(total)
final_amount=total-discount_amount+GST_amount+delivery

print("products:",total)
print("discount:",discount_amount)
print("GST:",GST_amount)
print("delivery:",delivery)
print("final_amount:",final_amount)
        
