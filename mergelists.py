

class Node:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next= next
        

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

#helper function for creating linked list
def create_linked_list(elements):
    if not elements:
        return None
    head = Node(elemements[0])
    current = head
    for value in elements[1:]:
        current.next = Node(value)
        current = current.next
        return head

#helper print function
def print_list():
    while node:
        print(node.data, end = " -> ")
        node = node.next
    print("None")
    
def main():
    list_1 = create_linked_list([2, 10, 5, 12, 44, 1])
    print_list(list1)

if __name__ == "__main__":
    main()