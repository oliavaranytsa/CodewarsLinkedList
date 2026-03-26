def get_nth(node, index):
        current = node
        i = 0

        while current is not None:
            if i == index:
                return current
            current = current.next
            i+= 1

        raise Exception("Invalid index")