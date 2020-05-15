class Node:
    def __init__(self, value=None, link=None):
        self.value = value
        self.link = link

    def get_value(self):
        return self.value

    def get_link(self):
        return self.link


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        # enqueue an item at the rear (back) of list (furthest to the left)
        data = Node()
        data.value = value
        if (self.front == None):
            self.front = data
        else:
            self.rear.link = data

        self.rear = data
        self.rear.link = self.front

    def dequeue(self):
        # dequeue an item from front of list (furthest to the right)
        if self.front == None:
            return None

        value = None
        if (self.front == self.rear):
            value = self.front.value
            self.front = None
            self.rear = None

        else:
            data = self.front
            value = data.value
            self.front = self.front.link
            self.rear.link = self.front

        return value
