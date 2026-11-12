# given a single linked list find its moddle node. if two middle nodes give the second one
from fcntl import FASYNC

from Patterns.Linked_Lists.Linked_list_core import LinkedList

def find_mid_point_last(mylist):
    slow = fast = mylist.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    print(slow.data)

def find_mid_point_first(mylist):
    slow = fast = mylist.head
    while fast and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    print(slow.data)

if __name__ == "__main__":
    l1 = LinkedList()
    l1.insert_at_end(1)
    l1.insert_at_end(2)
    l1.insert_at_end(4)
    l1.insert_at_end(7)
    l1.insert_at_end(3)

    l2 = LinkedList()
    l2.insert_at_end(1)
    l2.insert_at_end(2)
    l2.insert_at_end(4)
    l2.insert_at_end(7)

    find_mid_point_last(l1)
    find_mid_point_first(l2)