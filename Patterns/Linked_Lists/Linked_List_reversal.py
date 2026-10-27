from Linked_list_core import LinkedList


def linked_list_reversal(ll):

    # place the pointers

    curr_node = ll.head
    prev_node = None

    # here comes the loop
    while curr_node:
        # create this pointer
        next_node = curr_node.next

        # move the current nodes pointer to prev node
        curr_node.next = prev_node

        # move current node to the next node
        prev_node = curr_node
        curr_node = next_node

    ll.head = prev_node
    return ll


if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(4)
    ll.insert_at_end(7)
    ll.insert_at_end(3)


    print("After insertions:")
    ll.print_list()

    reversed_l1 = linked_list_reversal(ll)
    reversed_l1.print_list()

