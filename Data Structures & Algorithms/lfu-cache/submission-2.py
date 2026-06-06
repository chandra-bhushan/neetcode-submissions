class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.freq = 1
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

        self.size = 0

    def insert(self, node: Node):
        prev_node = self.right.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.right
        self.right.prev = node

        self.size += 1

    def remove(self, node: Node):
        if self.size == 0:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_last(self) -> Node:
        if self.size == 0:
            return None
        node = self.left.next
        self.remove(node)
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lfu = 1
        self.store = {}
        self.freq_map = defaultdict(LinkedList)
        

    def __update_freq(self, node: Node):
        cur_freq = node.freq
        cur_ll = self.freq_map[cur_freq]
        cur_ll.remove(node)
        self.freq_map[cur_freq + 1].insert(node)

        if node.freq == self.lfu and cur_ll.size == 0:
            self.lfu += 1
        
        node.freq += 1


    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        node = self.store[key]
        self.__update_freq(node)

        return node.value
        
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.store:
            # updating an existing node
            node = self.store[key]
            node.value = value
            self.__update_freq(node)
            return
        
        if len(self.store) == self.capacity:
            cul_ll = self.freq_map[self.lfu]
            removed_node = cul_ll.remove_last()
            del self.store[removed_node.key]
            
        node = Node(key, value)
        self.freq_map[1].insert(node)
        self.store[key] = node
        self.lfu = 1


        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)