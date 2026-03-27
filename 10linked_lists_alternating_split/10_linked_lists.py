def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError("List must have at least two nodes.")

    first_head = None
    first_tail = None
    second_head = None
    second_tail = None

    current = head
    toggle = True

    while current:
        next_node = current.next
        current.next = None

        if toggle:
            if first_head is None:
                first_head = current
                first_tail = current
            else:
                first_tail.next = current
                first_tail = current
        else:
            if second_head is None:
                second_head = current
                second_tail = current
            else:
                second_tail.next = current
                second_tail = current

        toggle = not toggle
        current = next_node

    return Context(first_head, second_head)