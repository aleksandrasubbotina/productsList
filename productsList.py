# Creates a string in JSON format: each element contains unique product ID
def products(count):
    result = ""
    for i in range(count):
        result += f'{{"id": {i+1}, "quantity": 1}}, '
    return result[:-2]

# Creates a string in JSON format with unique IDs
def ids(count):
    result = ""
    for i in range(count):
        result += str(i+1) + ", "
    return result[:-2]

# Creates full request body in JSON format: name of the list and its contents
def productsList(count):
    return f'{{"productsList":[{products(count)}]}}'

# Creates body for another request were only IDs are needed
def idList(count):
    return f'{{"ids":[{ids(count)}]}}'

print(productsList(5))

print(idList(3))