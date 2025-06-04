class circularQueue:

    CAPACITY = 10

    def __init__(self):
        self._data = [None] * circularQueue.CAPACITY
        self._size = 0
        self._front = 0 # This is a positional argument

    def isEmpty(self):
        if self._size == 0:
            return True
        else:
            return False

    def enqueue(self, element):
        if self._size == len(self._data):
            self.resize(2* len(self._data))

        tail = (self._front + self._size) % len(self._data)
        self._data[tail] = element
        self._size += 1

    def dequeue(self):
        if self.isEmpty(): # Check first if there is anything in the queue
            raise empty("Queue is empty")
        dequeued = self._data[self._front] # Get the element at the location of the head
        front = self._front + 1 % len(self._data)
        self._data[self._front] = None # Update the location of the head and give it none
        self._size -= 1 # Reduce the size of elements in the list
        return dequeued # Give back the dequeued element

    def resize(self, capacity: int):
        pass

    def first(self):
        if self.isEmpty():
            raise empty("Queue is empty")
        else:
            return self._data[self._front]

class empty(Exception):
    ...

if __name__ == '__main__':
    object_queue = circularQueue()

    insert_elements = [1,2,3,4,5,6]

    for i in insert_elements:
        object_queue.enqueue(i)
        print(f'You have added {i}. ')
        print(f'The length of the queue is {object_queue._size}')
        print("")
