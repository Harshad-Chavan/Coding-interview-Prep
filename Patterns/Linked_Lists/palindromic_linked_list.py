from operator import indexOf
from tarfile import HeaderError

from Linked_list_core import LinkedList

def find_mid(input_list):
    slow = fast = input_list.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def reverse_list(head):
    curr = head
    prev = None

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev


def palindromic_linked_list(inp_list):

    mid = find_mid(inp_list)
    reverse_list_head = reverse_list(mid)

    ptr1 = inp_list.head
    ptr2 = reverse_list_head

    while ptr1 != ptr2:
        if ptr1.data == ptr2.data:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        else:
            return False
    return True

if __name__ == "__main__":
    l1 = LinkedList()

    l1.insert_at_end(1)
    l1.insert_at_end(2)
    l1.insert_at_end(3)
    l1.insert_at_end(2)
    l1.insert_at_end(1)

    l1.print_list()

    print(palindromic_linked_list(l1))