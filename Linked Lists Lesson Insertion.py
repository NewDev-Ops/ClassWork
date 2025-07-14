#Making the node
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Making a linkedlist class
class linkedlist:
    def __init__(self):
        self.top = None

#Making the insertion method for the linkedlist
    def insert_into_the_list(self, data):
        addition_is = node(data)

        if self.top == None:
            self.top = addition_is
            return

        current = self.top
        while current.next:
            current = current.next
        current.next = addition_is

#Printing out the list
    def print_linked_list(self):
        position = self.top
        while position:
            print(position.data)
            position = position.next

testlist = linkedlist()
testlist.insert_into_the_list(5)
testlist.insert_into_the_list(10)
testlist.insert_into_the_list(15)

testlist.print_linked_list()



