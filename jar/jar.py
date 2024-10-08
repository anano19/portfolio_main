class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity is less than 0")
        self._size = 0
        self._capacity = capacity



    def __str__(self):
        return "🍪" * self._size


    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Too many cookies")
        else: self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("not enough cookies")
        else:
            self._size -= n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
