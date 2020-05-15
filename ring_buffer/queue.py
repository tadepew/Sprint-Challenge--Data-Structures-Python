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
        new_node = Node(value)

        if self.rear is not None:
            self.rear.link = new_node
        else:
            self.front = new_node

        # replace previous rear with new node
        self.rear = new_node
        # make new rear's link the front to complete circle
        new_node.link = self.front

        return self.rear.value

    def dequeue(self):
        # dequeue an item from front of list (furthest to the right)

        if self.front is not None:
            deleted = self.front.value
            self.front = self.front.link

        else:
            deleted = None

        return deleted

    def display(self):
        while self.rear != self.front:
            print(self.front.value, end=", ")
            self.front = self.front.link
        print(self.front.value)
