
#Creation of a singly linked list
from symtable import *

class SinglyLinked:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode


snode1 = SinglyLinked(1)
snode2 = SinglyLinked(2)
snode3 = SinglyLinked(3)
snode4 = SinglyLinked(4)

snode1.nextNode = snode2
snode2.nextNode = snode3
snode3.nextNode = snode4

currentnode = snode1

#Method one
while currentnode:
    print(currentnode.value, ">>>", end= " ")
    currentnode = currentnode.nextNode


