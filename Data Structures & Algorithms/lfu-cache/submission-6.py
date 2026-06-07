class _Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v

        self.freq = 1

        self.prev = self.next = None


class _LinkedList:
    def __init__(self):
        self.left = self.right = _Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def insert(self, node: _Node):
        # always happens at right
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

        self.size += 1

    def remove(self, node: _Node):
        if self.size == 0:
            return
        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1

    def remove_last(self) -> _Node:
        if self.size == 0:
            return None
        # remove lru
        node = self.left.next
        self.remove(node)

        return node



class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lfu = 1
        self.store = {}
        self.freq_map = defaultdict(_LinkedList) # {0 -> ll}

    def __update_freq(self, node: _Node):
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
            # already exists. just update freq
            node = self.store[key]
            node.value = value # update value
            self.__update_freq(node)
            return
        
        if len(self.store) == self.capacity:
            evict_ll = self.freq_map[self.lfu]
            evict_node = evict_ll.remove_last()
            del self.store[evict_node.key]

        # if we came here that means we are adding a new node which is not seen before
        # it must be added on lfu = 1
        node = _Node(key, value)
        self.store[key] = node
        
        self.freq_map[1].insert(node)
        self.lfu = 1
        

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)