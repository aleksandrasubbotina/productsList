# Creates a string in JSON format: each element contains unique product ID
def idAndQuantity(count):
    result = ""
    for i in range(count):
        result += f'{{"id": {i+1}, "quantity": 1}}, '
    return result[:-2]

#Creates list of products with quantity from a list
def productsFromList(list):
    result = ""
    for i in list:
        result += f'{{"id": {i}, "quantity": 1}}, '
    return result[:-2]

# Creates a string in JSON format with unique IDs
def ids(count):
    result = ""
    for i in range(count):
        result += str(i+1) + ", "
    return result[:-2]

# Creates full request body with product ids in ascending order and their quantity
def productsBody(count):
    return f'{{"productsList":[{idAndQuantity(count)}]}}'

# Creates full request body with product ids from input list and their quantity
def productsFromListBody(list):
    return f'{{"productsList":[{productsFromList(list)}]}}'

# Creates body for another request were only IDs are needed
def idListBody(count):
    return f'{{"ids":[{ids(count)}]}}'

print(productsBody(2))

#print(idListBody(20))

#print(productsFromListBody([6,7,9,10,11,12,14,15,16,18]))