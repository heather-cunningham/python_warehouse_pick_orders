#Heather Cunningham
#MCC Python 3.6 Online
#Prof. Brown-Sederberg
#FINAL

#Order STACK CLASS
import sys
from order_class import Order

class OrderStack:
    def __init__(self):
        self.items = []
    #------METHS---------------

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

    def print_stack(self):
        li = 1
        for item in self.items:
            print("\n\nLine Item: " + str(li))
            li += 1
            print(item)
        #print(self.items)

    def get_length(self):
        return len(self.items)
