import numpy as np
import matplotlib.pyplot as plt

def initialize_weights(input_dim, grid_dim):
    return np.random.rand(grid_dim[0], grid_dim[1], input_dim)

def find_bmu(pattern, SOM):
    distances = np.linalg.norm(SOM - pattern, axis=2)
    return np.unravel_index(np.argmin(distances), distances.shape)

def update_weights(SOM, pattern, bmu, learning_rate, neighborhood_radius):
    for i in range(SOM.shape[0]):
        for j in range(SOM.shape[1]):
            distance = np.linalg.norm(np.array([i, j]) - np.array(bmu))
            if distance <= neighborhood_radius:
                influence = np.exp(-distance ** 2 / (2 * (neighborhood_radius ** 2)))
                SOM[i, j] += learning_rate * influence * (pattern - SOM[i, j])

def train_SOM(dataset, SOM, num_iterations, learning_rate, neighborhood_radius):
    for _ in range(num_iterations):
        for pattern in dataset:
            bmu = find_bmu(pattern, SOM)
            update_weights(SOM, pattern, bmu, learning_rate, neighborhood_radius)

# Generate sample data
X, y = np.random.rand(100, 3), np.random.randint(0, 2, 100)

# Initialize SOM
input_dim = X.shape[1]
grid_dim = (10, 10)
SOM = initialize_weights(input_dim, grid_dim)

# Train SOM
learning_rate = 0.5
neighborhood_radius = 2.0
num_iterations = 1000
train_SOM(X, SOM, num_iterations, learning_rate, neighborhood_radius)

# Define and initialize matrices to 0
mapa_clasificacion = np.zeros(grid_dim + (input_dim,))
mapa_activaciones = np.zeros(grid_dim)
mapa_distancias = np.zeros(grid_dim)

# Classify patterns and calculate activation and distances maps
for pattern in X:
    bmu = find_bmu(pattern, SOM)
    print("Patrón:", pattern, "Coordenadas de la BMU:", bmu)
    mapa_clasificacion[bmu] = pattern
    mapa_activaciones[bmu] += 1
    mapa_distancias[bmu] += np.linalg.norm(SOM[bmu] - pattern)

mapa_distancias /= mapa_activaciones

# Calculate number of classes
num_classes = len(np.unique(y))
print("Número de clases:", num_classes)

# Draw classification, activation, and distances maps
plt.imshow(mapa_clasificacion, interpolation='nearest', aspect='auto')
plt.title("Mapa de Clasificación")
plt.show()

plt.imshow(mapa_activaciones, interpolation='nearest', aspect='auto')
plt.title("Mapa de Activaciones")
plt.show()

plt.imshow(mapa_distancias, interpolation='nearest', aspect='auto')
plt.title("Mapa de Distancias")
plt.show()

# Calculate Quantization Error and Topological Error
U = np.zeros(grid_dim)
for i in range(grid_dim[0]):
    for j in range(grid_dim[1]):
        neighbors = []
        if i > 0:
            neighbors.append(SOM[i - 1, j])
        if i < grid_dim[0] - 1:
            neighbors.append(SOM[i + 1, j])
        if j > 0:
            neighbors.append(SOM[i, j - 1])
        if j < grid_dim[1] - 1:
            neighbors.append(SOM[i, j + 1])
        U[i, j] = np.mean([np.linalg.norm(SOM[i, j] - neighbor) for neighbor in neighbors])

qe = np.mean(U)
te = len(np.where(U > 1.0)[0]) / (grid_dim[0] * grid_dim[1])

print("Error de cuantificación:", qe)
print("Error Topológico:", te)
