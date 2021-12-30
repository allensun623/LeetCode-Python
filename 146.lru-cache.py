'''
LRU 算法的淘汰策略是 Least Recently Used，也就是每次淘汰那些最久没被使用的数据；
LFU 算法的淘汰策略是 Least Frequently Used，也就是每次淘汰那些使用次数最少的数据
https://labuladong.github.io/algo/2/20/44/

Double Linked Node
'''

class LinkedNode:
  def __init__(self, key, val):
    self.key = key
    self.val = val
    self.prev = None
    self.next = None
    
class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.cache = {}
    self.head = LinkedNode(0, 0)
    self.tail = LinkedNode(0, 0)
    self._connect(self.head, self.tail)
    # self.head.next = self.tail
    # self.tail.prev = self.head
    
  def get(self, key: int) -> int:
    '''get the value of node by key, if not exists, return -1'''
    if key not in self.cache:
      return -1
    node = self.cache[key]
    self.put(key, self.cache[key].val)
    return node.val
    
  def put(self, key: int, val: int) -> None:
    '''
    update the val to node key if exists, and move to last,
    if not exits, add node to the last
    '''
    if key in self.cache:
      self._remove_node(key)

    self._add(key, val)
    
  def _update(self, key: int, val: int) -> None:
    '''update value'''
    self._remove_node(key)
    self._add(key, val)
      
  def _add(self, key: int, val: int) -> None:
    '''add node to the end'''
    node = LinkedNode(key, val)
    self._connect(self.tail.prev, node)
    self._connect(node, self.tail)
    # node.prev = self.tail.prev
    # node.next = self.tail
    # self.tail.prev.next = node
    # self.tail.prev = node
    self.cache[node.key] = node
    if len(self.cache) > self.capacity:
      self._remove_first()
    
  def _remove_last(self) -> None:
    '''remove the last node'''
    key = self.tail.prev.key
    self._connect(self.tail.prev.prev, self.tail) 
    # self.tail.prev = self.tail.prev.prev
    # self.tail.prev.next = self.tail  
    del self.cache[key]
    
  def _remove_first(self) -> None:
    '''remove the first node'''
    key = self.head.next.key
    self._connect(self.head, self.head.next.next)
    # self.head.next = self.head.next.next
    # self.head.next.prev = self.head
    del self.cache[key]
    
  def _remove_node(self, key: int) -> None:
    '''remove specific node if exists'''
    if key not in self.cache:
      return None

    node = self.cache[key]
    self._connect(node.prev, node.next)
    # node.prev.next = node.next
    # node.next.prev = node.prev
    del self.cache[key]
  
  def _connect(self, p: LinkedNode, n: LinkedNode):
    p.next, n.prev = n, p

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

