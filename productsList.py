def id_list(count):
    result = ""
    for i in range(count):
        new_element = f'{{"id": {i+1}, "quantity": 1}}, '
        result += new_element
    #return (f"\{'productsList':\[{result[:-2]}\]\}")
    return result[:-2]

def productsList(count):
    return f'{{"productsList":[{id_list(count)}]}}'

def idList(count):
    return f'{{"ids":[{id_list(count)}]}}'

print(productsList(15))
