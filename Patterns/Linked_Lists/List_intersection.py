from Linked_list_core import LinkedList


def linked_list_intersection(l1,l2):
     ptr_a, ptr_b = l1.head, l2.head
     while ptr_a != ptr_b:
         ptr_a = ptr_a.next if ptr_a else l2.head
         ptr_b = ptr_b.next if ptr_b else l1.head

     print(ptr_a.data)



if __name__ == '__main__':
    l1 = LinkedList()
    l2 = LinkedList()

    l1.insert_at_beginning(4)
    l1.insert_at_beginning(3)
    l1.insert_at_beginning(2)
    l1.insert_at_beginning(1)

    l2.insert_at_beginning(7)
    l2.insert_at_beginning(6)
    l2.insert_at_beginning(5)

    i = l2.head
    while i.next:
        i = i.next

    j = l1.head
    while j.data != 3:
        j = j.next

    i.next = j

    l1.print_list()
    l2.print_list()

    linked_list_intersection(l1,l2)

