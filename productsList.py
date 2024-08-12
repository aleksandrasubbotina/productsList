# Creates a string in JSON format: each element contains unique product ID
def id_list(count):
    result = ""
    for i in range(count):
        new_element = f'{{"id": {i+1}, "quantity": 1}}, '
        result += new_element
    return result[:-2]

# Creates full request body in JSON format: name of the list and its contents
def productsList(count):
    return f'{{"productsList":[{id_list(count)}]}}'

# Creates body for another request were only IDs are needed
def idList(count):
    return f'{{"ids":[{id_list(count)}]}}'

print(productsList(5))

print(idList(3))