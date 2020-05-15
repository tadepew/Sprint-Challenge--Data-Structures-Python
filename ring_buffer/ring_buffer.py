from queue import Queue


class RingBuffer:
    def __init__(self, capacity):
        # fixed size
        # when full, oldest element overwritten with newest (LRU)
        self.capacity = capacity
        self.size = 0
        self.data = Queue()

    def append(self, item):
        # adds given elements to buffer in given order

        if self.size == self.capacity:
            self.data.dequeue()
            self.size -= 1

        self.data.enqueue(item)
        self.size += 1

    def get(self):
        cur = self.data.front

        while cur:
            print(cur.value)
            cur = cur.link
            if cur == self.data.front:
                break
        # temp = self.data.front
        # while temp is not self.data.front.link:
        #     print(temp.link.get_value())
        #     temp = temp.get_link()
