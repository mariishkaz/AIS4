def dfs(graph, start, end, visited=None): #функция обхода в глубина
    if visited is None: #проверка пути
        visited = [start]
    if start == end: #проверка конца
        return visited #комментарий 1
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, end, visited + [neighbor])
            if new_path:
                return new_path
    return visited
def validate_vertices(graph, start, end):
    if start not in graph:
        raise ValueError(f"Стартовая вершина {start} отсутствует в графе.")
    if end not in graph:
        raise ValueError(f"Конечная вершина {end} отсутствует в графе.")

def main():
    # Определение графа
    graph = {
        1: [3],
        2: [4],
        4: [2]
    }
    
    # Ввод начальной и конечной вершин
    try:
        a = int(input("Введите стартовую вершину (a): "))
        b = int(input("Введите конечную вершину (b): "))
        
        # Проверка корректности вершин
        validate_vertices(graph, a, b)
        
        # Поиск пути
        path = dfs(graph, a, b)
        if path:
            print(f"Путь: {path}")
            print(f"Длина пути: {len(path) - 1}")
        else:
            print("Путь не найден.")
    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()