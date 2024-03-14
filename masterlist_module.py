#Heather Cunningham
#MCC Python 3.6 Online
#Prof. Brown-Sederberg
#FINAL

#MasterList Mod
import re
from order_class import Order

def create_MasterList(ordersFile):
    """creates 1 master List of all order objects in this batch, in this
    orders' .txt file, sorted by aisle #"""
    master_list = []
    while True:
        #new_line is a str Of the list in it
        new_line = ordersFile.readline()
        if len(new_line) == 0:
            break
        str_list = re.split("([^0-9])", new_line)
        new_list = []
        for el in str_list:
            if el.isdigit():
                new_list.append(int(el))
        new_list.reverse()
        master_list.append(new_list)
        Orders_List = orders_Master(master_list)
        Orders_List = sort_orders_by_aisle(Orders_List)
    return Orders_List

def orders_Master(master_list):
    Orders_List = []
    for each_list in master_list:
        new_order = Order(each_list[0],each_list[1],each_list[2],
                          each_list[3], each_list[4], each_list[5])
        Orders_List.append(new_order)
    return Orders_List
            
## Sort orders_Master list of objects by aisle #
def sort_orders_by_aisle(Orders_List):
    for i in range(len(Orders_List) ):
        for j in range(len(Orders_List) -1):
            if Orders_List[i].aisle_num > Orders_List[j].aisle_num:
                tempOrder = Orders_List[i]
                Orders_List[i] = Orders_List[j]
                Orders_List[j] = tempOrder
    return Orders_List

def print_Master(Orders_List):
    li = 1
    for order in Orders_List:
        print("\n\nLine Item: " + str(li))
        li += 1
        print(order)

    
                
        
