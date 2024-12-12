import random

def ant_colony_tsp(graph, num_ants, num_iterations, alpha=1, beta=2, evaporation_rate=0.5):
    n = len(graph)
    pheromones = [[1 for _ in range(n)] for _ in range(n)]
    best_route = None
    best_cost = float('inf')

    def probability(i, j, visited):
        numerator = (pheromones[i][j] ** alpha) * ((1 / graph[i][j]) ** beta)
        denominator = sum(
            (pheromones[i][k] ** alpha) * ((1 / graph[i][k]) ** beta)
            for k in range(n) if k not in visited and graph[i][k] > 0
        )
        return numerator / denominator if denominator > 0 else 0

    for _ in range(num_iterations):
        all_routes = []
        for ant in range(num_ants):
            visited = [0]
            while len(visited) < n:
                current = visited[-1]
                next_city = max(
                    ((j, probability(current, j, visited)) for j in range(n) if j not in visited),
                    key=lambda x: x[1],
                    default=(None, 0)
                )[0]
                if next_city is not None:
                    visited.append(next_city)
            all_routes.append(visited + [0])

        for route in all_routes:
            cost = sum(graph[route[i]][route[i+1]] for i in range(n))
            if cost < best_cost:
                best_cost = cost
                best_route = route

        # Обновление феромонов
        for i in range(n):
            for j in range(n):
                pheromones[i][j] *= (1 - evaporation_rate)

        for route in all_routes:
            cost = sum(graph[route[i]][route[i+1]] for i in range(n))
            for i in range(n):
                pheromones[route[i]][route[i+1]] += 1 / cost

    return best_route, best_cost

# Пример графа и вызова
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
best_route, best_cost = ant_colony_tsp(graph, num_ants=10, num_iterations=100)
print("Лучший маршрут:", best_route)
print("Стоимость маршрута:", best_cost)
