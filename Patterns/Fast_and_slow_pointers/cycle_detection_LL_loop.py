from tarfile import HeaderError

from Patterns.Linked_Lists.Linked_list_core import LinkedList

def cycle_detection_hash_set(mylist):

    visited_node = set()
    ptr = mylist.head
    while ptr.next:
        print(ptr.data)
        if ptr.data in visited_node:
            return True
        visited_node.add(ptr.data)
        ptr =  ptr.next

    return False

def cycle_detection(mylist):
    slow = fast = mylist.head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False


if __name__ == '__main__':
    l1 = LinkedList()

    l1.insert_at_end(0)
    l1.insert_at_end(1)
    l1.insert_at_end(2)
    l1.insert_at_end(3)
    l1.insert_at_end(4)
    l1.insert_at_end(5)

    tail = l1.head
    while tail.next:
        tail = tail.next

    myptr = l1.head
    while myptr.data != 2:
        myptr = myptr.next

    tail.next = myptr

    print(cycle_detection_hash_set(l1))
    print(cycle_detection(l1))