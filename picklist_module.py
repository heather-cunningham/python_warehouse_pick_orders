#Heather Cunningham
#MCC Python 3.6 Online
#Prof. Brown-Sederberg
#FINAL

#PickList Mod
from order_class import Order

## Sort pick_list of objects by shelf #
def sort_by_shelf_n_bin(pick_list):
    for i in range(len(pick_list) ):
        for j in range(len(pick_list) -1):
            if pick_list[i].shelf_num > pick_list[j].shelf_num:
                tempOrder = pick_list[i]
                pick_list[i] = pick_list[j]
                pick_list[j] = tempOrder
            if pick_list[i].shelf_num == pick_list[j].shelf_num:
                if pick_list[i].bin_num < pick_list[j].bin_num:
                    tempOrder = pick_list[i]
                    pick_list[i] = pick_list[j]
                    pick_list[j] = tempOrder
    return pick_list
