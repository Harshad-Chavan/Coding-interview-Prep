from Linked_list_core import LinkedList

def remove_kth_last_value(inp_list : LinkedList, k):
    # since we have inserted at the begining its laready marked as head
    inp_list.insert_at_beginning(-1)
    trailer, leader = inp_list.head, inp_list.head

    # Edge case if the head node itself is to be deleted
    # move the sec ptr k steps ahead of 1st ptr a
    for i in range(0,k):
        leader = leader.next

    while leader.next:
        trailer = trailer.next
        leader = leader.next

    # do the magic an remove the element
    trailer.next = trailer.next.next
    inp_list.head = inp_list.head.next

    inp_list.print_list()


if __name__ == "__main__":
    LL = LinkedList()


    LL.insert_at_end(1)
    LL.insert_at_end(2)
    LL.insert_at_end(3)
    LL.insert_at_end(4)
    LL.insert_at_end(5)


    LL.print_list()

    remove_kth_last_value(LL,2)

