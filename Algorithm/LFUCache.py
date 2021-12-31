from collections import defaultdict
class Node:
  '''Double linked Node'''
  def __init__(self, key: int, val: int):
    self.key = key
    self.val = val
    self.freq = 0
    self.prev = None
    self.next = None

class DoubleLinkedList:
  '''Double Linked List, add new node to the end before tail'''
  def __init__(self, freq: int):
    self.size = 0
    self.freq = freq
    self.head = Node(0, 0)
    self.tail = Node(0, 0)
    self._connect(self.head, self.tail)
    
  def put(self, node: Node) -> None:
    self._connect(self.tail.prev, node)
    self._connect(node, self.tail)
    self.size += 1
    
  def remove_node(self, node: Node) -> None:
    self._connect(node.prev, node.next)
    self.size -= 1
  
  def _connect(self, p: Node, n: Node) -> None:
    p.next, n.prev = n, p
    
class LFUCache:
  '''
  node_cache = {node key: node}
  freq_cache = {freq key: node freq}
  '''
  def __init__(self, capacity: int):
    self._capacity = capacity
    self._min_freq = 0
    self._size = 0
    self._node_cache = {}
    self._freq_cache = {}
    
  def get(self, key: int) -> int:
    if key not in self._node_cache:
      return -1
    # 1. get node
    node = self._node_cache[key]
    # 2. remove node
    self._remove_node(node)
    # 3. update node
    self._update(node)
    
    return node.val
    
  
  def put(self, key: int, val: int) -> None:
    if self._capacity == 0:
      return None
    # 1. if key not in the node cache, create new one
    if key not in self._node_cache:
      # if size of nodes == capacity, remove the least frequent and oldest node
      if self._size == self._capacity:
        self._remove_least_frequently_used()
      node = Node(key, val)
      self._node_cache[key] = node
      self._min_freq = 0
    # 2. if key in node cache, update
    else:
      node = self._node_cache[key]
      node.val = val
      self._remove_node(node)
    
    self._update(node)
  
  def _remove_least_frequently_used(self) -> None:
    '''remove the least frequently and oldest node'''
    node = self._freq_cache[self._min_freq].head.next
    self._remove_node(node)
    del self._node_cache[node.key]
  
  def _remove_node(self, node: Node) -> None:
    '''2. remove target node'''
    node_freq = self._freq_cache[node.freq]
    # remove node from current frequency link, and remove frequency node if it is empty
    node_freq.remove_node(node)
    if node_freq.size == 0:
      del self._freq_cache[node.freq]
    self._size -= 1
  
  def _update(self, node: Node) -> None:
    '''3. update node'''
    # update the current min freq
    if self._min_freq == node.freq and node.freq not in self._freq_cache:
      self._min_freq += 1
    # increase the frequency by 1
    node.freq += 1
    # create a new frequency node if not exists, else add node to frequency link
    if node.freq not in self._freq_cache:
      node_freq = DoubleLinkedList(node.freq)
    else:
      node_freq = self._freq_cache[node.freq]
    # update node in its freq link and freq in freq cache
    node_freq.put(node)
    self._freq_cache[node.freq] = node_freq
    self._size += 1
    
    
# ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]

lfu = LFUCache(2)
assert lfu.put(1, 1) == None
assert lfu.put(2, 2) == None
assert lfu.get(1) == 1
assert lfu.put(3, 3) == None
assert lfu.get(2) == -1
assert lfu.get(3) == 3
assert lfu.put(4, 4) == None
assert lfu.get(1) == -1
assert lfu.get(3) == 3
assert lfu.get(4) == 4
print('Pass!')
