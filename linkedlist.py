#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        self.size = 0
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(self.as_list())

    def as_list(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        # TODO: count number of items
        return self.size

    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        # Creates a new Node
        node = Node(item)
        # Checks if the LinkedList is empty
        if self.is_empty():
            # Adds the new node to the head
            self.head = node
        # If a tail already exists, add a new tail
        if self.tail is not None:
            self.tail.next = node
        # If a tail doesn't exist, add tail
        self.tail = node
        # Increments the size of the LinkedList
        self.size += 1

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        # Creates a new Node
        node = Node(item)
        # Checks if the LinkedList is empty
        if self.is_empty():
            self.head = node
            self.tail = node
        # If a head already exists, create a variable that holds the head
        # This is so that we can still have access to the items in linked list
        temp, temp.next = self.head, self.head.next
        self.head, self.head.next = node, temp
        self.size += 1

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        # TODO: find given item and delete if found
        node = Node(item)
        index = self.as_list().index(item)
         # If linked list is empty
        if self.head is None:
            return
        if self.tail is None:
            return

        # Store head node
        temp = self.head

        # If head needs to be removed
        if index == 0:
            self.head = temp.next
            if self.tail is None:
                self.tail = None
            else:
                self.tail = 
            self.size -= 1
            temp = None
            return

        # If position is more than number of nodes
        if temp is None:
            return
        if temp.next is None:
            return

        # Node temp.next is the node to be deleted
        # store pointer to the next of node to be deleted
        next = temp.next.next

        # Unlink the node from linked list
        temp.next = None

        temp.next = next
        self.size -= 1


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # TODO: find item where quality(item) is True
        print(type(quality))
        if quality in self.as_list():
            print("testing")
        return False


def test_linked_list():
    ll = LinkedList()
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())
    '''
    print("===================")
    ll.prepend('C')
    ll.prepend('B')
    ll.prepend('A')
    print('List: ', ll)
    print('tail ', ll.tail)
    print("===================")

    print(">>>>>>>>>>>>>>>>>>>>")
    ll.find(lambda item: item == 'B') == 'B'
    print('List: ', ll)
    print(">>>>>>>>>>>>>>>>>>>>")
    '''
    ll.delete('A')
    print('tail: ' + str(ll.tail))
    print(ll)
    ll.delete('C')
    print('tail: ' + str(ll.tail))
    print(ll)
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())


if __name__ == '__main__':
    test_linked_list()
