
from stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        if self.value > value:
            # if tree node is greater than value to insert, go left
            if self.left:
                # works recursively and returns true
                return self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)

        else:
            # if tree node is less than or equal to value to insert, go right
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # when we start searching self will be the root
        # with recursion we always need to define our criteria for stopping
        if target == self.value:
            return True  # cascades back up

        if target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)

        if target > self.value:
            if not self.right:
                return False
            return self.right.contains(target)

        # else:
        #     return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()

        else:
            return self.value

        # Call the function `fn` on the value of each node

    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
