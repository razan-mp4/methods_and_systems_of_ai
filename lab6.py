import pygame
import sys
import numpy as np

# Ініціалізація pygame
pygame.init()

# Налаштування екрану
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Агенти з нейронними мережами")

class Agent:
    def __init__(self):
        self.input_layer_neurons = 2
        self.hidden_layer_neurons = 2
        self.output_neurons = 1
        self.hidden_weights = np.random.uniform(size=(self.input_layer_neurons, self.hidden_layer_neurons))
        self.hidden_bias = np.random.uniform(size=(1, self.hidden_layer_neurons))
        self.output_weights = np.random.uniform(size=(self.hidden_layer_neurons, self.output_neurons))
        self.output_bias = np.random.uniform(size=(1, self.output_neurons))
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def feedforward(self, inputs):
        self.hidden_layer_activation = np.dot(inputs, self.hidden_weights) + self.hidden_bias
        self.hidden_layer_output = self.sigmoid(self.hidden_layer_activation)
        self.output_layer_activation = np.dot(self.hidden_layer_output, self.output_weights) + self.output_bias
        return self.sigmoid(self.output_layer_activation)
    
    def train(self, inputs, expected_output, epochs=10000, lr=0.1):
        for _ in range(epochs):
            predicted_output = self.feedforward(inputs)
            error = expected_output - predicted_output
            d_predicted_output = error * self.sigmoid_derivative(predicted_output)
            error_hidden_layer = d_predicted_output.dot(self.output_weights.T)
            d_hidden_layer = error_hidden_layer * self.sigmoid_derivative(self.hidden_layer_output)
            self.output_weights += self.hidden_layer_output.T.dot(d_predicted_output) * lr
            self.output_bias += np.sum(d_predicted_output, axis=0, keepdims=True) * lr
            self.hidden_weights += inputs.T.dot(d_hidden_layer) * lr
            self.hidden_bias += np.sum(d_hidden_layer, axis=0, keepdims=True) * lr

agent = Agent()

inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
expected_output = np.array([[0], [1], [1], [0]])

def display_text(screen, text, position):
    font = pygame.font.Font(None, 24)
    text_surf = font.render(text, True, (10, 10, 10))
    screen.blit(text_surf, position)

# Основний цикл
running = True
epoch_count = 0
training = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                training = not training
    
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (400, 300), 50)
    
    display_text(screen, "Нейронна мережа агента", (50, 50))
    display_text(screen, f"Hidden Weights: {agent.hidden_weights.tolist()}", (50, 100))
    display_text(screen, f"Hidden Bias: {agent.hidden_bias.tolist()}", (50, 150))
    display_text(screen, f"Output Weights: {agent.output_weights.tolist()}", (50, 200))
    display_text(screen, f"Output Bias: {agent.output_bias.tolist()}", (50, 250))
    
    initial_prediction = agent.feedforward(inputs)
    display_text(screen, f"Initial Prediction: {initial_prediction.tolist()}", (50, 300))
    
    if training:
        agent.train(inputs, expected_output, epochs=100)
        epoch_count += 100
    
    final_prediction = agent.feedforward(inputs)
    display_text(screen, f"Final Prediction: {final_prediction.tolist()}", (50, 350))
    display_text(screen, f"Epochs Trained: {epoch_count}", (50, 400))
    display_text(screen, "Press 'S' to start/stop training", (50, 450))
    
    pygame.display.flip()
    
pygame.quit()
sys.exit()
