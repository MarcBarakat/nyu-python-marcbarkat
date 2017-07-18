import code
import datetime
import os
import os.path
import csv
from collections import OrderedDict

init_question = "Please specify which operation you would like to perform:"
ok_responses = {'List','Show','Create','Update','Destroy','Quit'}
cwd = os.getcwd()
csv_file_path = cwd +'\\..\\data\\products.csv'
def PrintDictRow(row):
#    print_str = ""
#    for key in row.keys():
#        print_str = print_str +row[key].ljust(1)
    print(row)

def LookupIdFromList(data_list, data_id):
    matching_data = [data for data in data_list if data["id"] == data_id]
    return matching_data[0]

def GetMaxId(data_list):
    max_id = 0
    for datum in data_list:
        max_id = max(max_id, int(datum["id"]))
    return(max_id)

def ListProducts(data):
    for datum in data:
        PrintDictRow(datum)

def ShowProduct(data, product_id):
    print(LookupIdFromList(data, product_id))

def CreateProduct(data):
    print("Please specify the product's information ")
    name = input("Please enter product name: ")
    aisle = input("Please input the product aisle: ")
    department = input("Please input the product department: ")
    price = input("Please input the product price: ")
    id = GetMaxId(data)
    return(OrderedDict([('id',str(id)),('name',name), ('aisle',aisle), ('department', department), ('price', price)]))

def DestroyProduct(data, product_id):
    data[:] = [d for d in data if d.get('id') != product_id]
    return(data)

def UpdateProduct(data):
    product_id = input("Please input the product id")
    product_data = LookupIdFromList(data, product_id)
    print("Please specify the product's information ")
    name = input("Change name from: " + product_data["name"]+" to: ")
    aisle = input("Change aisle from: " + product_data["aisle"]+" to: ")
    department = input("Change department from: " + product_data["department"]+" to: ")
    price = input("Change price from: " + product_data["price"]+" to: ")
    updated_product = OrderedDict([('id',str(id)),('name',name), ('aisle',isle), ('department', department), ('price', price)])
    DestroyProduct(data, product_id)
    data.append(updated_product)
    return(data)

with open(csv_file_path, "r+") as csv_file:
    csv_reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
    data = list(csv_reader)
    csv_writer = csv.writer(csv_file)

n_prods = len(data)
print('--------------------------------------------------')
print('PRODUCTS APPLICATION')
print('--------------------------------------------------\n')

print("There are " + str(n_prods) + " products in the database. Please select an operation")
init_question = "operation | description\n"
init_question = init_question + "---------- | -----------\n"
init_question = init_question + "'List'     | Display a List of product identifier and names\.\n"
init_question = init_question + "'Show'     | Show information about a product\.\n"
init_question = init_question + "'Create'   | Add a new product\.\n"
init_question = init_question + "'Update'   | Edit an existing product\.\n"
init_question = init_question + "'Destroy'  | Delete an existing product\.\n"
init_question = init_question + "'Quit'     | Exit the program\.\n"

init_question = init_question + "\n"
init_response = input(init_question)
while(init_response!="Quit"):
    if(init_response in ok_responses):
        if(init_response=="List"):
            ListProducts(data)
            init_response = input(init_question)
        elif(init_response=="Show"):
            show_response = input("Please specify a product id")
            ShowProduct(data, show_response)
            init_response = input(init_question)
        elif(init_response=="Create"):
            new_product = CreateProduct(data)
            data.append(new_product)
            csv_writer.writerows(data)
            init_response = input(init_question)
        elif(init_response=="Destroy"):
            show_response = input("Please specify a product id")
            data = DestroyProxduct(data, show_response)
            csv_writer.writerows(data)
            init_response = input(init_question)
        elif(init_response=="Update"):
            show_response = input("Please specify a product id")
            data = UpdateProduct(data, show_response)
            csv_writer.writerows(data)
            init_response = input(init_question)
    else:
        print("Please provide a valid response")
        init_response = input(init_question)
