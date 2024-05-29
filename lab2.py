import random
import numpy as np

# Відстані між містами (матриця ваг)
distances = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

# Параметри генетичного алгоритму
population_size = 100
mutation_rate = 0.01
num_generations = 500

# Ініціалізація популяції
def initialize_population(size, num_cities):
    population = []
    for _ in range(size):
        individual = list(np.random.permutation(num_cities))
        population.append(individual)
    return population

# Обчислення пристосованості
def fitness(individual, distances):
    total_distance = 0
    for i in range(len(individual)):
        total_distance += distances[individual[i]][individual[(i+1) % len(individual)]]
    return 1 / total_distance

# Відбір батьків (турнірний відбір)
def select_parents(population, fitnesses):
    parents = []
    for _ in range(len(population)):
        tournament = random.sample(list(zip(population, fitnesses)), 3)
        parents.append(max(tournament, key=lambda x: x[1])[0])
    return parents

# Кросовер (часткове зіставлення)
def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [None] * len(parent1)
    child[start:end] = parent1[start:end]
    ptr = 0
    for gene in parent2:
        if gene not in child:
            while child[ptr] is not None:
                ptr += 1
            child[ptr] = gene
    return child

# Мутація (обмін двох генів)
def mutate(individual, rate):
    if random.random() < rate:
        i, j = random.sample(range(len(individual)), 2)
        individual[i], individual[j] = individual[j], individual[i]

# Основна функція генетичного алгоритму
def genetic_algorithm(distances, population_size, mutation_rate, num_generations):
    num_cities = len(distances)
    population = initialize_population(population_size, num_cities)
    for generation in range(num_generations):
        fitnesses = [fitness(individual, distances) for individual in population]
        parents = select_parents(population, fitnesses)
        next_population = []
        for i in range(0, len(parents), 2):
            parent1, parent2 = parents[i], parents[i + 1]
            child1, child2 = crossover(parent1, parent2), crossover(parent2, parent1)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            next_population.extend([child1, child2])
        population = next_population
    best_individual = max(population, key=lambda x: fitness(x, distances))
    return best_individual, 1 / fitness(best_individual, distances)

# Запуск генетичного алгоритму
best_path, best_distance = genetic_algorithm(distances, population_size, mutation_rate, num_generations)
print(f"Найкращий маршрут: {best_path}")
print(f"Відстань: {best_distance}")
