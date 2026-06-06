class Node:
    def __init__(self, k, v):
        self.key = k
        self.value = v

        self.freq = 1

        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.left = Node(0, 0)
        self.right = Node(0, 0)

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
            return None
        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1

    def remove_last(self) -> Node:
        if self.size == 0:
            return None
        node_to_remove = self.left.next
        self.remove(node_to_remove)

        return node_to_remove



class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lfu_index = 1 # test with 1
        self.store = {}
        self.freq_map = defaultdict(LinkedList) # {0: LinkedList}
        
    def update_freq(self, node: Node):
        cur_freq = node.freq
        cur_ll = self.freq_map[cur_freq]
        cur_ll.remove(node)
        self.freq_map[cur_freq + 1].insert(node)

        if cur_ll.size == 0 and self.lfu_index == cur_freq:
            self.lfu_index += 1
        
        node.freq +=1

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        
        node = self.store[key]
        self.update_freq(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.store:
            node = self.store[key]
            node.value = value
            self.update_freq(node)
            return

        if len(self.store) == self.capacity:
            # need to evict
            cur_ll = self.freq_map[self.lfu_index]
            node_to_remove = cur_ll.remove_last()
            del self.store[node_to_remove.key]

        new_node = Node(key, value)
        self.freq_map[1].insert(new_node)
        self.store[key] = new_node
        self.lfu_index = 1
        
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)