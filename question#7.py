def get_min_and_max(list_items):
    #sort the list using lambda
    sorted_list = sorted(list_items, key=lambda x:x)
    min_value = min(sorted_list)
    max_value = max(sorted_list)
    
    return max_value, min_value


print(get_min_and_max([8,90,1,34,45,3,56,21]))