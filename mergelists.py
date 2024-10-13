from typing import Optional

class Node:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next= next
        

class Solution:
    def mergeTwoLists(self, list_1: Optional[Node], list_2: Optional[Node]) -> Optional[Node]:
        dummy = Node()
        current = dummy
        
        while list_1 and list_2:
            if list_1.data < list_2.data:
                current.next = list_1
                list_1 = list_1.next
            else:
                current.next = list_2
                list_2 = list_2.next
            current = current.next
        if list_1:
            current.next = list_1
        elif list_2:
            current.next = list_2
            
        return dummy.next

#helper function for creating linked list
def create_linked_list(elements):
    if not elements:
        return None
    head = Node(elements[0])
    current = head
    for value in elements[1:]:
        current.next = Node(value)
        current = current.next
    return head

#helper print function
def print_list(node):
    while node:
        print(node.data, end = " -> ")
        node = node.next
    print("None")
    
def main():
    list_1 = create_linked_list([1, 3, 5])
    list_2 = create_linked_list([2, 4, 7])
    
    solution = Solution()
    merge = solution.mergeTwoLists(list_1, list_2)
   
    print_list(merge)
   

if __name__ == "__main__":
    main()