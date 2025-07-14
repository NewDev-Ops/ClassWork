from calendar import firstweekday
#Creation of a singly linked list OOP implementation
from symtable import *

#Insertion at the Beginning
class Node_OOP_implementation:
    def __init__(self, data):
        self.input = data
        self.next_address = None

class Linkedlist:
    def __init__(self):
        self.head = None

    #Method to insert the head
    def inserthead(self, newdata):
        newnode = Node_OOP_implementation(newdata)
        newnode.next_address = self.head
        self.head = newnode

    def insertend(self, newdata):
        newnode = Node_OOP_implementation(newdata)
        infront = self.head

        ##Check if list is empty
        if infront is None:
            self.head = newnode
            return

        # If not empty, look at the first node (what is infront), look at it as last and then push forward to the next addrress

        last = infront
        while last.next_address != None:
            last = last.next_address
        last.next_address = newnode

    #Delete from the beginning
    def delete_from_head(self):
        if self.head is None:
            return "The list is empty"
        self.head = self.head.next_address

    def delete_from_end(self):

        if self.head is None:
            print("The list is empty")

        if self.head.next_address is None:
            self.head.next_address = None
            return

        temp = self.head
        while temp.next_address.next_address:
            temp = temp.next_address
        temp.next_address = None

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.input, ">>>", end=" ")
            temp = temp.next_address
        print()

if __name__ == "__main__":
    llist = Linkedlist()
    llist.inserthead(10)
    llist.inserthead(5)
    llist.inserthead(0)
    llist.insertend(15)
    llist.delete_from_head()
    llist.delete_from_end()
    llist.printlist()