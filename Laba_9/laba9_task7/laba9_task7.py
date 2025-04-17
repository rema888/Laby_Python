import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

species = iris[:, -1]

# Нахождение уникальных значений и их количества
unique_species, counts = np.unique(species, return_counts=True)

print("Уникальные виды ирисов:")
for species, count in zip(unique_species, counts):
    print(f"{species.decode('utf-8')}: {count} экземпляров")