import random

# Текстовий корпус на тему "Історія розвитку штучного інтелекту"
corpus = """
The history of artificial intelligence (AI) began in antiquity, with myths, stories and rumors of artificial beings endowed with intelligence or consciousness by master craftsmen. As technological advances created computers in the mid-20th century, it became possible to create programs that performed complex tasks.
In 1950, Alan Turing proposed the Turing Test as a criterion of intelligence, and in 1956, the Dartmouth Conference established AI as a field. Researchers developed algorithms, such as Arthur Samuel's checkers player and the Logic Theorist. 
The 1980s brought expert systems, the first successful form of AI software. In the 1990s and 2000s, AI developed further with advances in machine learning, robotics, and computer vision. Today, AI is a part of everyday life, from search engines to autonomous cars.
"""

# Підготовка тексту
words = corpus.split()

# Створення біграмної моделі
bigrams = {}
for i in range(len(words) - 1):
    if words[i] not in bigrams:
        bigrams[words[i]] = []
    bigrams[words[i]].append(words[i + 1])

# Функція для генерації тексту
def generate_text(start_word, num_words):
    current_word = start_word
    text = [current_word]
    for _ in range(num_words - 1):
        if current_word in bigrams:
            next_word = random.choice(bigrams[current_word])
            text.append(next_word)
            current_word = next_word
        else:
            break
    return ' '.join(text)

# Генерація тексту
start_word = "The"
num_words = 100
generated_text = generate_text(start_word, num_words)

# Створення HTML сторінки
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>History of Artificial Intelligence</title>
</head>
<body>
    <h1>History of Artificial Intelligence</h1>
    <p>{generated_text}</p>
</body>
</html>
"""

# Збереження HTML сторінки у файл
with open("history_of_ai2.html", "w") as file:
    file.write(html_content)

print("HTML page generated and saved as 'history_of_ai.html'.")
