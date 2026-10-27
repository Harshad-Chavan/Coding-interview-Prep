class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # ---------- Insertion ----------
    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def insert_at_position(self, data, position):
        """Insert at a 0-based index."""
        if position < 0:
            raise IndexError("Position cannot be negative")
        if position == 0:
            self.insert_at_beginning(data)
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        if current is None:
            raise IndexError("Position out of range")
        node = Node(data)
        node.next = current.next
        current.next = node

    # ---------- Deletion ----------
    def delete_by_value(self, value):
        """Delete the first node with the given value. Returns True if deleted."""
        if self.head is None:
            return False
        if self.head.data == value:
            self.head = self.head.next
            return True
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def delete_at_position(self, position):
        """Delete the node at a 0-based index."""
        if self.head is None or position < 0:
            raise IndexError("Position out of range")
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(position - 1):
            if current.next is None:
                raise IndexError("Position out of range")
            current = current.next
        if current.next is None:
            raise IndexError("Position out of range")
        current.next = current.next.next

    # ---------- Other helpers ----------
    def search(self, value):
        current, index = self.head, 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1

    def __len__(self):
        count, current = 0, self.head
        while current:
            count += 1
            current = current.next
        return count

    # ---------- Printing ----------
    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        parts = []
        while current:
            parts.append(str(current.data))
            current = current.next
        print(" -> ".join(parts) + " -> None")


if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_beginning(5)
    ll.insert_at_position(15, 2)
    print("After insertions:")
    ll.print_list()          # 5 -> 10 -> 15 -> 20 -> 30 -> None

    ll.delete_by_value(20)
    print("After deleting value 20:")
    ll.print_list()          # 5 -> 10 -> 15 -> 30 -> None

    ll.delete_at_position(0)
    print("After deleting position 0:")
    ll.print_list()          # 10 -> 15 -> 30 -> None

    print("Index of 15:", ll.search(15))
    print("Length:", len(ll))