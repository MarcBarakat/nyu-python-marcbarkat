import code
import datetime
import os
import os.path


def PrintReceipt(receipt, time_string):
    return_string = ""
    return_string=return_string+"-------------------------------------\n"
    return_string=return_string+"MY GROCERY STORE\n"
    return_string=return_string+"-------------------------------------\n"
    return_string=return_string+"Web: wwww.mystore.com\n"
    return_string=return_string+"Phone: 1.123.456.7890\n"
    return_string=return_string+"Checkout Time: " + time_string +"\n"
    return_string=return_string+"-------------------------------------\n"
    return_string=return_string+"Shopping Cart Items:\n"
    total = 0
    for item in receipt:
        return_string=return_string+"+ " + item["name"] + " ($" + str('%.2f' % round(item["price"],2)) + ")\n"
        total=total+item["price"]
    return_string=return_string+"-------------------------------------\n"
    return_string=return_string+"Subtotal: $" + str('%.2f' % round(total,2)) + "\n"
    return_string=return_string+"Plus NYC Sales Tax (8.875%): $" + str('%.2f' % round(0.08875 * total,2)) + "\n"
    return_string=return_string+"Total: $" + str('%.2f' % round(1.08875 * total,2)) + "\n"
    return_string=return_string+"-------------------------------------\n"
    return_string=return_string+"Thanks for your business! Please come again\n"
    return(return_string)
    pass


products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # Products based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017
products_dict = {}
for product in products:
    products_dict[product["id"]] = product


product_ids =[]
input_question = "Please input a product identifier, or 'DONE' if there are no more items "
product_id = input(input_question)
while(product_id!="DONE"):
    product_ids.append(product_id)
    product_id = input(input_question)
receipt = []
for product_id in product_ids:
    print(products_dict[int(product_id)]["name"])
    receipt.append({"name":products_dict[int(product_id)]["name"],"price":products_dict[int(product_id)]["price"] })
current_time = datetime.datetime.now()
date_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(date_str)
receipt_string = PrintReceipt(receipt, date_str)
cwd = os.getcwd()
directory = cwd +'\\receipts\\'
try:
    os.stat(directory)
except:
    os.mkdir(directory)
file_name =   current_time.strftime("%Y-%m-%d-%H-%M-%S-%f") + '.txt'
completeName = os.path.join(directory,file_name)

file = open(completeName, "w")
file.write(receipt_string)
file.close()

print(receipt_string)
