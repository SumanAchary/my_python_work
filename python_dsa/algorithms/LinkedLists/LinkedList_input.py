class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# this is the implemented function definition
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
        print(head.data)
        head = head.next


head = take_input()

print(print_linked_list(head))
