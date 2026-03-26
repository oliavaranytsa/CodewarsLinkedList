
def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == "None":
        return None

    parts = list_repr.split (" -> ")[:-1]
    head = None
    for value in reversed(parts):
        head = Node(int(value), head)
    return head