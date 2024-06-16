import numpy as np

# Налаштування параметрів
num_cities = 5
num_ants = 10
num_iterations = 100
alpha = 1.0
beta = 2.0
evaporation_rate = 0.5
pheromone_constant = 100.0

# Відстані між містами (симетрична матриця)
distance_matrix = np.array([
    [0, 2, 2, 5, 7],
    [2, 0, 4, 8, 2],
    [2, 4, 0, 1, 3],
    [5, 8, 1, 0, 2],
    [7, 2, 3, 2, 0]
])

# Ініціалізація феромонів
pheromone_matrix = np.ones((num_cities, num_cities)) / num_cities

# Ініціалізація мурах
class Ant:
    def __init__(self, num_cities):
        self.num_cities = num_cities
        self.visited = []
        self.distance_traveled = 0.0

    def visit_city(self, city):
        if self.visited:
            self.distance_traveled += distance_matrix[self.visited[-1], city]
        self.visited.append(city)

    def reset(self):
        self.visited = []
        self.distance_traveled = 0.0

# Функція для вибору наступного міста
def select_next_city(ant, pheromone_matrix, alpha, beta):
    current_city = ant.visited[-1]
    probabilities = []

    for next_city in range(num_cities):
        if next_city not in ant.visited:
            pheromone = pheromone_matrix[current_city, next_city] ** alpha
            heuristic = (1.0 / distance_matrix[current_city, next_city]) ** beta
            probabilities.append(pheromone * heuristic)
        else:
            probabilities.append(0.0)

    probabilities = probabilities / np.sum(probabilities)
    return np.random.choice(range(num_cities), p=probabilities)

# Основний цикл алгоритму
best_route = None
best_distance = float('inf')

for iteration in range(num_iterations):
    ants = [Ant(num_cities) for _ in range(num_ants)]

    # Ініціалізація мурах в випадкових містах
    for ant in ants:
        initial_city = np.random.randint(0, num_cities)
        ant.visit_city(initial_city)

    # Рух мурах по містам
    for ant in ants:
        while len(ant.visited) < num_cities:
            next_city = select_next_city(ant, pheromone_matrix, alpha, beta)
            ant.visit_city(next_city)
        # Повернення в початкове місто
        ant.visit_city(ant.visited[0])

    # Оновлення феромонів
    pheromone_matrix *= (1.0 - evaporation_rate)
    for ant in ants:
        for i in range(len(ant.visited) - 1):
            from_city = ant.visited[i]
            to_city = ant.visited[i + 1]
            pheromone_matrix[from_city, to_city] += pheromone_constant / ant.distance_traveled

    # Пошук найкращого маршруту
    for ant in ants:
        if ant.distance_traveled < best_distance:
            best_distance = ant.distance_traveled
            best_route = ant.visited

print(f"Найкращий маршрут: {best_route} з відстанню {best_distance}")
