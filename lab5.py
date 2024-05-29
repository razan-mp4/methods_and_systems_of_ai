import numpy as np

# Приклад векторів ознак (покупки різних товарів)
feature_vectors = np.array([
    [1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0, 0]
])

# Параметри алгоритму
rho = 0.5  # Параметр уважності
beta = 1.0  # Параметр схожості

# Функція для обчислення схожості
def similarity(v1, v2):
    return np.sum(np.minimum(v1, v2)) / (beta + np.sum(v2))

# Функція для перевірки параметру уважності
def vigilance(v1, v2, rho):
    return np.sum(np.minimum(v1, v2)) / np.sum(v1) >= rho

# Алгоритм ART1
def art1(feature_vectors, rho, beta):
    prototypes = []
    clusters = []

    for vector in feature_vectors:
        matched = False
        for i, prototype in enumerate(prototypes):
            if similarity(vector, prototype) > rho and vigilance(vector, prototype, rho):
                prototypes[i] = np.minimum(vector, prototype)
                clusters[i].append(vector)
                matched = True
                break
        if not matched:
            prototypes.append(vector)
            clusters.append([vector])

    return prototypes, clusters

# Виконання алгоритму ART1
prototypes, clusters = art1(feature_vectors, rho, beta)

# Виведення результатів
print("Прототипи кластерів:")
for proto in prototypes:
    print(proto)

print("\nКластери:")
for cluster in clusters:
    print(cluster)


# Функція для рекомендації товарів
def recommend_products(new_vector, prototypes, clusters):
    for i, prototype in enumerate(prototypes):
        if similarity(new_vector, prototype) > rho and vigilance(new_vector, prototype, rho):
            cluster = clusters[i]
            all_products = np.sum(cluster, axis=0)
            recommended_products = np.where(all_products > 0, 1, 0)
            return recommended_products
    return np.zeros_like(new_vector)

# Новий покупець
new_customer = np.array([0, 1, 0, 1, 0, 0])

# Рекомендація товарів
recommendation = recommend_products(new_customer, prototypes, clusters)
print("\nРекомендовані товари:")
print(recommendation)
