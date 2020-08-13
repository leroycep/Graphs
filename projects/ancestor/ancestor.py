
def earliest_ancestor(ancestors, starting_node):
    graph = {}

    # Build graph of children's parents
    for (parent, child) in ancestors:
        if child in graph:
            graph[child].add(parent)
        else:
            graph[child] = {parent}

    next_verts = [(0, starting_node)]
    visited = set()
    oldest = next_verts[0]
    while len(next_verts) > 0:
        depth, current = next_verts.pop()

        # TODO: Handle case where there are multiple paths to the ancestor that differ in length
        if current in visited:
            continue
        visited.add(current)

        if depth > oldest[0] or depth == oldest[0] and current < oldest[1]:
            oldest = (depth, current)

        if current not in graph:
            continue

        for parent in graph[current]:
            next_verts.append((depth + 1, parent))

    if oldest[1] == starting_node:
        return -1
    return oldest[1]
