#Heather Cunningham
#MCC Python 3.6 Online
#Prof. Brown-Sederberg
#FINAL

#Order

class Order:
    def __init__(self, bin_num=0, shelf_num=0, aisle_num=0, qty=0, pt_num=0,
                 order_num=0):
        self.bin_num = bin_num
        self.shelf_num = shelf_num
        self.aisle_num = aisle_num
        self.qty = qty
        self.pt_num = pt_num
        self.order_num = order_num
    #----------METHODS------------------------------------------------------------
    #to_str
    def __str__(self):
        return "\n------------\nOrder #: {0}\n------------\nLOCATION:\nAisle #: {1}  Shelf #: {2}  Bin #: {3}\nORDER DETAILS:\nPart #: {4}  Qty = {5}".format(self.order_num,self.aisle_num,self.shelf_num,self.bin_num,self.pt_num,self.qty)

    def write_to_file(self):
        return "\n------------\nOrder #: {0}\n------------\nLOCATION:\nAisle #: {1}  Shelf #: {2}  Bin #: {3}\nORDER DETAILS:\nPart #: {4}  Qty = {5}".format(self.order_num,self.aisle_num,self.shelf_num,self.bin_num,self.pt_num,self.qty)
