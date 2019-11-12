import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.value = value
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        # self.value = value
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_tail()
        else:
            return None

    def len(self):
        # self.storage.length
        return self.size