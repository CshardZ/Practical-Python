from emoji import emojize

#  Challenge-11
def your_vat():
    while True:
        try:
            price, vat = int(input("Enter price: ")), float(input("Enter VAT Rate: "))
            break
        except:
            print("\nPlease enter valid price and VAT Rate(Percentage)")

    return f"Total price: { price + price*(vat/100) }"

print(your_vat())

def your_vat2():🤢😵
    print("\n\n\n")
    try:
        price, vat = int(input("Enter price: ")), float(input("Enter VAT Rate: "))
    except:
        price, vat = -1,101
        while (price<=0 or vat>100) and (price,vat != int, float):
            try:
                price, vat = int(input("Please enter valid price: ")), float(input(("Enter VAT Rate(Percentage): ")))
            except:
                print("\n!.VALUE/TYPE ERROR.! occured, Please read and input again.")
        
    return f"Total price: { price + price*(vat/100) }"

print(your_vat2())

# Extra
def test(rng):
    for  i in range(rng):
        print(emojize(":snake:")*i,'\n')

print(test(7))\
