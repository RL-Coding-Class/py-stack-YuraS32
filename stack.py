class Stack:
    def __init__(self, _type = None):
        self._items = []
        self._type = _type
    def push(self, k):
       self._items.append(k)
    def pop(self):
        if self._items == None:
            return None
        l = self._items[-1]
        del self._items[-1]
        return l
        #else:
         #   return None
    def length(self):
        return len(self._items)
    def get(self):
        return self._items[-1]
    def __str__(self):
        pass
    def __repr__(self):
        pass