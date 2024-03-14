#Heather Cunningham         5/11/17
#MCC Python 3.6 Online
#Prof. Brown-Sederberg
#FINAL

#Warehouse (MAIN)
from masterlist_module import*
from orderstack_class import OrderStack
from order_class import Order
from picklist_module import*

try:
    ordersFile = open("warehouse_data_final_exam_Python.txt")
except: 
    print("Can't find or open file named " + ordersFile)

#creates 1 master List of all order objects in this batch, in this orders' .txt file, sorted by aisle #
master_list = create_MasterList(ordersFile)
ordersFile.close()

try:
    picklist_file = open("picklist_data.txt", "w")
except: 
    print("Can't find or open file named " + picklist_file)


#creates 1 master Stack so orders can be pushed & popped in order of aisles
master_stack = OrderStack()
for order in master_list:
    master_stack.push(order)

pick_sz = 6
oda_num = 0
while not master_stack.is_empty():
    if master_stack.is_empty():
        break
    pick_list = []
    oda_num += 1
    if master_stack.get_length() < pick_sz:
        for i in range( master_stack.get_length() ):
            item = master_stack.pop()
            pick_list.append(item)
        pick_list = sort_by_shelf_n_bin(pick_list)
        print("\n\n-------------------")
        print("ODA employee#: " + str(oda_num))
        print("-------------------")
        picklist_file.write("\n\n-------------------")
        picklist_file.write("ODA employee#: " + str(oda_num))
        picklist_file.write("-------------------")
        li = 1
        for item in pick_list:
            print("\n\nLine Item: " + str(li))
            picklist_file.write("\n\n\nLine Item: " + str(li))
            li += 1
            item = item.write_to_file()
            picklist_file.write(item)
            print(item)
    else:
        for i in range(pick_sz):
            item = master_stack.pop()
            pick_list.append(item)
        pick_list = sort_by_shelf_n_bin(pick_list)
        print("\n\n-------------------")
        print("ODA employee#: " + str(oda_num))
        print("-------------------")
        picklist_file.write("\n\n-------------------")
        picklist_file.write("ODA employee#: " + str(oda_num))
        picklist_file.write("-------------------")
        li = 1
        for item in pick_list:
            print("\n\nLine Item: " + str(li))
            picklist_file.write("\n\n\nLine Item: " + str(li))
            li += 1
            item = item.write_to_file()
            picklist_file.write(item)
            print(item)
    

picklist_file.close()

###master_stack.print_stack()
###print_Master(master_list)
