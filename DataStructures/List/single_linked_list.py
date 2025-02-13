def new_list():
    newlist ={
        'first': None,
        'last': None,
        'size': 0,
    }
    return newlist


def get_element(my_list,pos):
    searchpos = 0 
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]


def is_present(my_list,element, cmp_function): 
    is_in_array = False
    temp = my_list['first']
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp['info']) == 0:
            is_in_array = True
        else:
            temp = temp['next']
            count += 1
            
    if not is_in_array:
        count = -1
    return count
    
    
def size(my_list):
    return my_list['size']


def add_first(my_list,element):
    
    dict_element = {}
    dict_element['info'] = element
    
    if my_list['first'] is None:
        my_list['first'] = dict_element
        my_list['last'] = dict_element
        dict_element['next'] = None

    else:
        dict_element['next'] = get_element(my_list,1)
        my_list['first'] = dict_element
    
    my_list['size'] += 1
        
    return my_list



def add_last(my_list,element):
    
    dict_element = {}
    dict_element['info'] = element
    dict_element['next'] = None
    
    if my_list['last'] == None:
        my_list['first'] = dict_element
        my_list['last'] = dict_element
    else:
        my_list['last']['next'] = dict_element
        my_list['last'] = dict_element
        
    my_list['size'] += 1
    return my_list

def first_element(my_list):
    return my_list['first']
    
    
    
    
    
