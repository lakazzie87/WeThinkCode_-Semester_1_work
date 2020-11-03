

def find_min(element):
    """TODO: complete for Step 1"""
    if len(element) == 1:
        return element[0]
    if element == []:
        return -1
    for item in element:
        if isinstance(item, int) == False:
            return -1
    element = sorted(element)
    del element [-1:]
    return find_min(element)    


def sum_all(element):
    """TODO: complete for Step 2"""
    if len(element) == 1:
        return element[0]
    if element == []:
        return -1
    for item in element:
        if isinstance(item, int) == False:
            return -1
    element[0] = element[0] + element[1]
    del element[1]
    return sum_all(element)


def find_possible_strings(character_set, n):
    """TODO: complete for Step 3"""
    
    #Base case
    for item in character_set:
        if isinstance(item, int) == True:
            return []
    if n == 1:
        return character_set
    else:
        # used on recursive cases
        new_list = []
        for element in character_set:
            char_list = find_possible_strings(character_set, n - 1)
            for new_element in char_list:
                new_list.append(element + new_element)
    return new_list


if __name__ == "__main__":      
   element = [1,2,3,4]
   character_set = ['x', 'y', 'z']
   n = 3
   print(find_min(element))
   print(sum_all(element))
   print(find_possible_strings(character_set, n))



