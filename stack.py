class Stack:
    def __init__(self, _type=None, _items=None):
        self._type = _type
        self._items = _items if _items is not None else []

    def push(self, k):
        self._items.append(k)

    def pop(self):
        if self._items == None:
            return None
        l = self._items[-1]
        del self._items[-1]
        return l

    def length(self):
        return len(self._items)

    def get(self):
        return self._items[-1]

    def __str__(self):
        return str(self._items)

    def __repr__(self):
        return f"Stack(_type={repr(self._type)}, _items={self._items})"
