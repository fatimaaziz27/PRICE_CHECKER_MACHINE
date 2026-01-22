#                                    PRICE CHECKING MACHINE
# A machine that takes user input for product name and tells the price of the product if it's available in the list

# PRODUCT DICTIONARY

products = {
    "Apple": 100,
    "Banana": 50,
    "Orange": 75,
    "Mango": 200,
    "Grapes": 150
}

# FUNCTION TO GET PRODUCT PRICE

def get_product_price(product_name):

    # CHECK IF PRODUCT IS IN THE DICTIONARY

    if product_name in products:
        return f"The price of {product_name} is {products[product_name]} PKR"

    # IF PRODUCT NOT FOUND

    else:
        return f"Sorry, {product_name} is not available or not for sale."

# MAIN LOOP

while True:

    # USER INPUT LOOP

    product_name = input("Enter product name (or 'quit' to stop): ")

    # IF USER WANTS TO QUIT

    if product_name.lower() == 'quit':
        break

    # PRINT PRODUCT PRICE

    print(get_product_price(product_name.capitalize()))

# END OF PROGRAM

