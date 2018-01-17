SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3

def check_lists(first_list, second_list):
    if first_list == second_list: return EQUAL
    for subList in [second_list[i:i+len(first_list)] for i in range(len(second_list))]:
        if first_list == subList: return SUBLIST
    for subList in [first_list[i:i+len(second_list)] for i in range(len(first_list))]:
        if second_list == subList: return SUPERLIST
    return UNEQUAL
