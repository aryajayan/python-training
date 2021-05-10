# This is an optional task.
# use string formatting functions to print an invoice like output

fname="Arya"
lname="Jayan"
invoiceNo="B1234"
itemList = [
    {'name':'Brinjal','price':30 },
    {'name':'Tomato','price':28 },
    {'name':'Onion','price':40 },
    {'name':'Potato','price':15 },
]

print("-------------------------------INVOICE-----------------------------")

print(f"Ms {fname} {lname}                      Invoice No: {invoiceNo}")
print()
print("Item                                           Price")
print()
total=0
for item in itemList:
    total+=item['price']
    print(f"{item['name']}                                         {item['price']}")

print(f"Total                                          {total}")