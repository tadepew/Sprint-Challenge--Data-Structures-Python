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
        new_node = Node()
        new_node.value = value
        if self.front == None:
            self.front = new_node
        else:
            # old self.rear's link is new node
            self.rear.link = new_node

        # replace previous rear with new node
        self.rear = new_node
        # make new rear's link the front to complete circle
        self.rear.link = self.front

    def dequeue(self):
        # dequeue an item from front of list (furthest to the right)
        if self.front == None:
            return None

        value = None
        if self.front == self.rear:
            value = self.front.value
            self.front = None
            self.rear = None

        else:
            node = self.front
            value = node.value
            self.front = self.front.link
            self.rear.link = self.front

        return value
