"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?
"""



class node(object):
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.maxSize = capacity
        self.curSize = 0
        self.pq = node(-1, -1)
        self.lastNode = None
        #holds the nodes
        self.val = dict() #hash set
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.val:
            curNode = self.val[key]
            #remove and append to the end of the pq
            prevNode = curNode.prev
            nextNode = curNode.next
            if self.lastNode != curNode:
                prevNode.next = nextNode
                nextNode.prev = prevNode
                self.lastNode.next = curNode
                curNode.prev = self.lastNode
                curNode.next = None
                self.lastNode = curNode
            return curNode.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        curNode = node(key, value)
        if key in self.val:
            self.val[key].val = value
            self.get(key)
            return
        
        if self.curSize == 0:
            self.pq.next = curNode
            curNode.prev = self.pq
            self.lastNode = curNode
            self.curSize+=1
        elif self.curSize < self.maxSize:
            self.lastNode.next = curNode
            curNode.prev = self.lastNode
            self.lastNode = curNode
            self.curSize+=1
        else:
            evicted = self.pq.next
            self.val.pop(evicted.key)
            if evicted != self.lastNode:
                self.pq.next = evicted.next
                evicted.next.prev = self.pq
                #appends a new node to the end of the linked list
                self.lastNode.next = curNode
                curNode.prev = self.lastNode
            else:
                self.pq.next = curNode
                curNode.prev = self.pq
            self.lastNode = curNode
        
        self.val[key] = curNode
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
