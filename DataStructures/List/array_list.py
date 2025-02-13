def new_list():
    newlist = {
        'elements': [],
        'size': 0,
    }
    return newlist



def get_element(my_list, index):
    
    return my_list['elements'][index]

def is_present(my_list,element, cmp_function):
    
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0,size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0 :
                keyexist = True
                break
        if  keyexist:
            return keypos
    return -1



def size(my_list):
    
    value = my_list['size']
    
    return value



def add_first(my_list,element):
    
    lista = my_list['elements']
    tamanio = my_list['size']
    
    lista.insert(0,element)
    tamanio += 1
    
    
def add_last(my_list,element):
    
    lista = my_list['elements']
    tamanio = my_list['size']
    
    lista.append(element)
    
    tamanio += 1
    
    
def first_element(my_list):
    
    lista = my_list['elements']
    
    return lista[0]

def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else:
        return False
        
