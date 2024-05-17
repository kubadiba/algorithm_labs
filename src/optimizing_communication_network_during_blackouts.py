import csv


class Graph:
    def __init__(self, vertices):
        """
        Ініціалізує граф з заданою кількістю вершин.

        Параметри:
        vertices (int): Кількість вершин у графі.
        """
        self.vertices = vertices
        self.edges = []

    def add_edge(self, source, destination, weight):
        """
        Додає ребро у граф.

        Параметри:
        source (int): Вершина, з якої виходить ребро.
        destination (int): Вершина, в яку входить ребро.
        weight (int): Вага ребра.
        """
        self.edges.append([source, destination, weight])

    def kruskal_minimum_spanning_tree(self):
        """
        Знаходить мінімальне остовне дерево за допомогою алгоритму Крускала.

        Повертає:
        int: Вага мінімального остовного дерева.
        """
        result = []
        edge_index = 0
        num_edges = 0

        # Сортуємо ребра графа за вагою в порядку зростання
        self.edges = sorted(self.edges, key=lambda item: item[2])

        parent = []
        rank = []

        # Ініціалізуємо множини для кожної вершини
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        # Вибираємо ребра, поки не утворимо мінімальне остовне дерево
        while num_edges < self.vertices - 1:
            source, destination, weight = self.edges[edge_index]
            edge_index += 1

            root_source = self.find(parent, source)
            root_destination = self.find(parent, destination)

            if root_source != root_destination:
                num_edges += 1
                result.append([source, destination, weight])
                self.union(parent, rank, root_source, root_destination)

        minimum_spanning_tree_weight = 0
        for source, destination, weight in result:
            minimum_spanning_tree_weight += weight

        return minimum_spanning_tree_weight


class DisjointSet:
    def find(self, parent, vertex_index):
        """
        Знаходить корінь дерева, до якого належить вершина.

        Параметри:
        parent (list): Список, що представляє батьків кожної вершини.
        vertex_index (int): Індекс вершини, для якої шукається корінь.

        Повертає:
        int: Корінь дерева, до якого належить вершина з вказаним індексом.
        """
        if parent[vertex_index] != vertex_index:
            parent[vertex_index] = self.find(parent, parent[vertex_index])
        return parent[vertex_index]

    def union(self, parent, rank, first_vertex, second_vertex):
        """
        Об'єднує два дерева в одне, враховуючи ранги.

        Параметри:
        parent (list): Список, що представляє батьків кожної вершини.
        rank (list): Масив рангів вершин.
        first_vertex (int): Перша вершина.
        second_vertex (int): Друга вершина.
        """
        if rank[first_vertex] < rank[second_vertex]:
            parent[first_vertex] = second_vertex
        elif rank[first_vertex] > rank[second_vertex]:
            parent[second_vertex] = first_vertex
        else:
            parent[second_vertex] = first_vertex
            rank[first_vertex] += 1


def read_communication_wells(filename):
    """
    Зчитує дані про комунікаційні колодязі з файлу CSV.

    Параметри:
    filename (str): Шлях до файлу CSV з даними.

    Повертає:
    list: Список кортежів з даними про ребра графа (джерело, призначення, вага).
    """
    graph_data = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            source, destination, weight = row[0], row[1], int(row[2])
            graph_data.append((source, destination, weight))
    return graph_data


def kruskal_minimum_spanning_tree(graph):
    """
    Знаходить мінімальне остовне дерево графа за допомогою алгоритму Крускала.

    Параметри:
    graph (list): Список кортежів з даними про ребра графа (джерело, призначення, вага).

    Повертає:
    int: Вага мінімального остовного дерева.
    """
    well_indices = {}
    num_wells = 0

    # Присвоюємо індекси кожному колодязю
    for edge in graph:
        if edge[0] not in well_indices:
            well_indices[edge[0]] = num_wells
            num_wells += 1
        if edge[1] not in well_indices:
            well_indices[edge[1]] = num_wells
            num_wells += 1

    g = Graph(num_wells)
    ds = DisjointSet()
    for edge in graph:
        source, destination, weight = edge[0], edge[1], edge[2]
        vertex_source, vertex_destination = (
            well_indices[source],
            well_indices[destination],
        )
        g.add_edge(vertex_source, vertex_destination, weight)

    min_cost = g.kruskal_minimum_spanning_tree()
    return min_cost


def main():
    """
    Головна функція для запуску програми.
    """
    file_path = "communication_wells.csv"
    graph = read_communication_wells(file_path)
    total_length = kruskal_minimum_spanning_tree(graph)
    if total_length != -1:
        print("Мінімальна довжина оптоволоконного кабелю:", total_length)
    else:
        print("Існують колодязі, які не з'єднані з іншими.")


if __name__ == "__main__":
    main()
