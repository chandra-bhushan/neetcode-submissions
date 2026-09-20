class Node:
    def __init__(self, key, value):
        self.next = None
        self.prev = None
        self.key = key
        self.value = value


class LinkedList:
    def __init__(self):
        self.head = self.tail = Node(0, 0)
        self.head.prev = self.tail
        self.tail.next = self.head

        self.size = 0

    def insert(self, node: Node):
        prev = self.head.prev

        self.head.prev = node
        node.prev = prev
        prev.next = node
        
        node.next = self.head
        self.head.prev = node

        self.size += 1

    def delete(self, node: Node):
        if self.size == 0:
            return None

        node.next.prev = node.prev
        node.prev.next = node.next

        self.size -= 1

    def delete_last(self):
        if self.size == 0:
            return None

        node = self.tail.next
        self.delete(node)
        return node


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {} # key: Node
        self.ll = LinkedList()
        

    def get(self, key: int) -> int:
        if key not in self.store.keys():
            return -1

        node = self.store[key]
        self.ll.delete(node)
        self.ll.insert(node)

        return node.value
       

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.store.keys():
            # updating existing key
            node = self.store[key]
            node.value = value
            self.ll.delete(node)
            self.ll.insert(node)
            return 

        if self.ll.size == self.capacity:
            eviction_node = self.ll.delete_last()
            del self.store[eviction_node.key]

        node = Node(key, value)
        self.store[key] = node

        self.ll.insert(node)

