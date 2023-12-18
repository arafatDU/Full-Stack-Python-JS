# shipping price of a shop
# if user are from ["Mirpur", "Farmgate", "Dhanmondi"] and purchased price >= 600 then shipping price free
# and purchased price >= 300 shipping price is 80 otherwise shipping price is 150
# And if user are from ["Mohakhali", "Gulshan"] and purchased price >= 800 shipping price is free
# For the rest of area, shipping is currently not available

print("------------------LIVE SHOPPING---------------\n---------Check your Shipping Charge-----------")
user_area = input("Where are you from? ")
total_purchased_price = int(input("Total purchased price: "))

if user_area in ["Mirpur", "Farmgate", "Dhanmondi"]:
    if total_purchased_price >= 600:
        print("Shipping is free")
    elif total_purchased_price >= 300:
        print("Shipping price 80 Tk")
    else:
        print("Shipping price 150 Tk")

elif user_area in ["Mohakhali", "Gulshan"]:
    if total_purchased_price >= 800:
        print("Shipping is free")
    elif total_purchased_price >= 500:
        print("Shipping price 100 TK")
    else:
        print("Shipping price 200 TK")

else:
    print("Shipping is currently not available!")
