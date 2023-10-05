class ListNode:
    #NOTHING CAN BE CHANGED HERE
    def __init__(self, val = 0, next= None):
        self.val = val
        self.next = next
         
            
############################################################
#  class  Slist
###########################################################   
class Slist():
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None
        self._len = 0 
    

class MyCircularQueue:
    def __init__(self, k: int):
        self._K = k
        self._s = Slist()

    def enQueue(self, value: int) -> bool:
        if self._s._len < self._K:
            newNode = ListNode(value)
            if self._s._first is None:
                self._s._first = self._s._last = newNode
            else:
                self._s._last.next = newNode
                self._s._last = newNode
            self._s._last.next = self._s._first
            self._s._len += 1
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self._s._first is not None:
            self._s._len -= 1
            if self._s._first == self._s._last:
                self._s._first = self._s._last = None
            else:
                self._s._last.next = self._s._first.next
                self._s._first = self._s._first.next
            return True
        else:
            return False

    def Front(self) -> int:
        return self._s._first.val if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self._s._last.val if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self._s._len == 0

    def isFull(self) -> bool:
        return self._s._len == self._K
