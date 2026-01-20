# A machine that takes user input for product name and tells the price of the product if it's available in the list

products = {
    "Apple": 100,
    "Banana": 50,
    "Orange": 75,
    "Mango": 200,
    "Grapes": 150
}

def get_product_price(product_name):
    if product_name in products:
        return f"The price of {product_name} is {products[product_name]} PKR"
    else:
        return f"Sorry, {product_name} is not available or not for sale."

while True:
    product_name = input("Enter product name (or 'quit' to stop): ")
    if product_name.lower() == 'quit':
        break
    print(get_product_price(product_name.capitalize()))


