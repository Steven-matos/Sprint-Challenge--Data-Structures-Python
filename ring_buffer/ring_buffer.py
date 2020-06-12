from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current = None

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
        else:
            if self.current == None or self.current.next == None:
                self.current = self.storage.head
            else:
                self.current = self.current.next
            self.current.value = item

    def get(self):
        list_contents = []

        node = self.storage.head
        while node != None:
            list_contents.append(node.value)
            node = node.next

        return list_contents
