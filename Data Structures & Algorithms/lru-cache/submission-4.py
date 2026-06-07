class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.left = self.right = None

class LinkedList:
    def __init__(self):
        self.left = self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def insert(self, node: Node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        
        self.size += 1

    def remove(self, node: Node):
        if self.size == 0:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
    
    def remove_last(self):
        if self.size == 0:
            return None

        node = self.left.next
        self.remove(node)
        return node


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}
        self.ll = LinkedList()
        

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        node = self.store[key]
        self.ll.remove(node)
        self.ll.insert(node)
        return node.value
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.store:
            node = self.store[key]
            self.ll.remove(node)
            node.value = value
            self.ll.insert(node)
            return

        if self.ll.size == self.capacity:
            evict_node = self.ll.remove_last()
            del self.store[evict_node.key]

        node = Node(key, value)
        self.store[key] = node
        self.ll.insert(node)
        
