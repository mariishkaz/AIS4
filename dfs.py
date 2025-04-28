def dfs(graph, start, end, visited=None):
    if visited is None:
        visited = [start]
    if start == end:
        return visited
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, end, visited + [neighbor])
            if new_path:
                return new_path
    return visited

graph = {4: [2], 1: [3], 2: [4]}
path = dfs(graph, 2, 4)
print(len(path) - 1 if path else "Нет пути")