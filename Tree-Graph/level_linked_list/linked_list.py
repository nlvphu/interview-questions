class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node object
        if self.head is None:  # If the list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Link the new node at the end

    def delete_node(self, key):
        current = self.head
        prev = None

        # If the node to be deleted is the head node
        if current and current.data == key:
            self.head = current.next  # Change head
            current = None
            return

        # Search for the key to be deleted
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not present in the linked list
        if current is None:
            return

        # Unlink the node from the linked list
        prev.next = current.next
        current = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")