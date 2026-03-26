def move_node(source, dest):
    if source is None:
        raise Exception("Source is empty")

    new_node = source
    source = source.next
    new_node.next = dest
    dest = new_node
    return Context(source, dest)