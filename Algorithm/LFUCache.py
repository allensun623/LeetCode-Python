class Node:
  '''Doubly linked Node'''
  def __init__(self, key: int, val: int, freq: int):
    self.key = key
    self.val = val
    self.freq = freq
    self.prev = None
    self.next = None

class DoubleLinkedNode:
  def __init__(self, heal_val: int = 0):
    self.size = 0
    self.freq = 0
    self.head = Node(heal_val, heal_val, 0)
  
  def get(self, key: int) -> int:
    pass
    
  def put(self, key: int, val: int) -> None:
    pass
    
  def _add(self, key: int, val: int) -> None:
    pass
    
  def _remove_node(self, key: int) -> None:
    pass
  
  def _remove_first_node(self) -> None:
    pass
    
    
  
  
  def _connect(self, p: Node, n: Node) -> None:
    p.next, n.prev = n, p
    
class LFUCache:
  '''
  node_cache = {node key: node}
  freq_cache = {node key: node freq}
  '''
  def __init__(self, capacity: int):
    self._capacity = capacity
    self._min_freq = 0
    self._size = 0
    self._node_cache = {}
    self._freq_cache = {}
    
  def __len__(self) -> int:
    return self._size
  
  def get(self, key: int) -> int:
    pass
  
  def put(self, key: int) -> int:
    pass