class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

# this is the implemented function definition
def insert_recursive(head, position, data):
     if position < 0:
         return head
     if position == 0:
         newNode = Node(data)
         newNode.next = head
         return newNode

     if head is None:
         return None
     small_head = insert_recursive(head.next,position-1,data)
     head.next = small_head
     return head


def take_input():
    input_list = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for curr_data in input_list:
        if curr_data == -1:
            break
        newNode = Node(curr_data)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head


def print_linked_list(head):
    if head is None:
        return head
    while head is not None:
        print(head.data, end=' --> ')
        head = head.next


head = take_input()
print(print_linked_list(head))
insert_recursive(head, 4, 45)
print("AFTER INSERTING 45 @ 4th position")
print(print_linked_list(head))
