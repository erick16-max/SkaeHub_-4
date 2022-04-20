#sorting a list of dict 

list_of_dict_data = [
    {'name':'tecno camon', 'price':23000,'color':'blue'},
    {'name':'samsung S21 plus', 'price':150000,'color':'black'},
    {'name':'iphone 13', 'price':147000,'color':'white'},
    {'name':'infinix note 8', 'price':18000,'color':'silver'}
]
    


#sorting the list of dict using the price
def sort_dict(dict_items):
    sorted_items = sorted(dict_items, key=lambda x:x['price'])
    return sorted_items

print(sort_dict(list_of_dict_data))