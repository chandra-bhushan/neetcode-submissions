class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.lru = Node(0,0)
        self.mru = Node(0,0)
        self.lru.next = self.mru
        self.mru.prev = self.lru

    def __delete(self, node: Node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def __insert(self, node: Node):
        prev = self.mru.prev
        node.next = self.mru
        self.mru.prev = node
        prev.next = node
        node.prev = prev

    def get(self, key: int) -> int:
        if key in  self.cache:
            value = self.cache[key].value
            # update lru and mru by delete and insert
            self.__delete(self.cache[key])
            self.__insert(self.cache[key])
            return value
        else: 
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.__delete(self.cache[key])       
        
        node = Node(key, value)
        self.cache[key] = node
        self.__insert(node)

        if len(self.cache) > self.capacity:
            # delete lru
            lru_node = self.lru.next            
            self.__delete(lru_node)
            del self.cache[lru_node.key]
        
