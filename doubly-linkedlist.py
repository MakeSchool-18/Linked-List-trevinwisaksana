
class Node(object):

    def __init__(self, data, previous):
        """Initialize this node with the given data"""
        self.data = data
        self.previous = previous
        self.next = None

    def set_data(self, d):
        """Used to set the data of the node, takes one argument"""
        self.data = d

    def set_next(self, n):
        """Used to set the node next to the current one, takes one argument"""
        self.next = n

    def set_previous(self, p):
        """Used to set the node before the current one, takes one argument"""
        self.previous = p

    def get_data(self):
        """Called to retrieve the data on the node"""
        return self.data

    def get_next(self):
        """Called to retrieve the node next to the current one"""
        return self.next

    def get_previous(self):
        """Called to get the node before the current one"""
        return self.previous

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

    def __iter__(self):
        """Allows the class to be iterable"""
        self.count = -1
        return self

    def next(self):
        '''Allows the iterable class to go iterate through elements'''
        if self.count < self.size:
            self.count += 1
        if self.count == self.size:
            raise StopIteration
        return self.as_list()[self.count]

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
        new_node = Node (item, self.head)
        # Checks if the LinkedList is empty
        if self.is_empty():
            self.head.set_previous(new_node)
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
        current = self.head
        previous = None

        while current is not None:
            if current.getData() is item:
                if self.head is current:
                    self.head = current.next
                if self.tail is current:
                    self.tail = previous
                if previous:
                    previous.next = current.next
                return
            previous = current
            current = current.next

        raise ValueError('Item not found: {}'.format(item))

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # TODO: find item where quality(item) is True
        for item in self.as_list():
            if quality(item) is True:
                return item
            if quality(item) is None:
                raise ValueError("Item not found")


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
    '''
    print(">>>>>>>>>>>>>>>>>>>>")
    print(ll)
    ll.find(lambda item: item == 'D')
    print('List: ', ll)
    print(">>>>>>>>>>>>>>>>>>>>")

    print("-------------------")
    print(ll)
    ll.delete('A')
    print('tail: ' + str(ll.tail))
    print(ll)
    ll.delete('C')
    print("What's left: ", ll)
    print('tail: ' + str(ll.tail))
    ll.delete('B')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print(ll.length())
    print("-------------------")
    '''
    print(ll)
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    for data in ll:
        print(data)
    '''
if __name__ == '__main__':
    test_linked_list()
