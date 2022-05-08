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


def insert(head, position, data):
    if position < 0 or position > length(head):
        return head
    count = 0
    curr = head
    prev = None
    while count < position:
        prev = curr
        curr = curr.next
        count += 1

    new_node = Node(data)
    if prev is not None:
        prev.next = new_node
    else:
        head = new_node
    new_node.next = curr
    return head


# this is the implemented function definition
def deleteNode(head, pos):
    # Write your code here.
    _length = length(head)
    if _length < pos or pos < 0:
        return head

    if pos == 0:
        # only when  the length of the linked list is greater than 0
        if _length > 0:
            head = head.next
            return head
        return None

    if pos == _length:
        return head

    curr = head
    prev = None
    count = 0
    while count < pos:
        prev = curr
        curr = curr.next
        count += 1

    prev.next = curr.next
    del curr
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
        print(head.data, end=" --> ")
        head = head.next


head = take_input()
print(print_linked_list(head))
insert(head, 4, 45)
print("AFTER INSERTING 45 @ 4th position")
print(print_linked_list(head))
print("AFTER DELETING @ 3th position")
deleteNode(head, 3)
print(print_linked_list(head))
