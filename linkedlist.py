class Node:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def create_linked_list(self, elements):
        if not elements:
            return None
        self.head = Node(elements[0])
        current = self.head
        for val in elements[1:]:
            current.next = Node(val)
            current = current.next
            
            
    def print_list(self):
        node = self.head
        while node:
            print(node.data, end = "->")
            node = node.next
        print("None")
        
        
    def add_to_start(self, node):
        node.next = self.head
        self.head = node
        
    def add_to_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    
def main():
    some_list = [1, 4, 5, 10, 2]
    
    linked_list = LinkedList()
    linked_list.create_linked_list(some_list)
    linked_list.print_list()
    print("\n")
    #adding to start
    linked_list.add_to_start(Node(99))
    linked_list.print_list()
    print("\n")
    #adding to end
    linked_list.add_to_end(144)
    linked_list.print_list()


if __name__ == "__main__":
    main()