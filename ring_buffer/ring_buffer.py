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
        # attempt 1
        # cur = self.data.front

        # while self.data.front != self.data.rear:
        #     print(cur.value, end=" ")
        #     cur = cur.link
        # print(self.data.rear.value)

        # attempt 2
        # temp = self.data.front
        # while temp is not self.data.front.link:
        #     print(temp.link.get_value())
        #     temp = temp.get_link()

        # if self.data:
        #     self.data.display()

        # return

        # current_node = self.data.front
        # values = []
        # while self.data.front:
        #     if self.data.front != self.data.rear:
        #         values.append(current_node.value)
        #     current_node = current_node.link
        #     values.append(current_node.value)
        #     return values

        # Note:  This is the only [] allowed
        values = []

        # TODO: Your code here
        current_item = self.data.front
        while current_item is not self.data.rear:
            values.append(current_item.value)
            current_item = current_item.link
        values.append(self.data.rear.value)
        # print(list_buffer_contents)
        return values
