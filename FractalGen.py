# Imports
import random
import matplotlib.pyplot as plt
import numpy as np

SIDE_LENGTH = 400 # Number of pixles to a side of the map.
FRACS = 2000 # Number of fractal lines applied to the map.
OCEAN_HEIGHT = 22 # The height at which the map changes the tiles to deep ocean color.


# Initializing the array
array = np.zeros((SIDE_LENGTH, SIDE_LENGTH))


def apply_line():
    """ Creates a random line intersecting the array and randomly chnages
        the altitude of the two halves by +1 and -1"""
    try:
        m = (np.random.randint(len(array)) - np.random.randint(len(array))) / (np.random.randint(len(array)) - np.random.randint(len(array)))
    except:
        m = 1
    b = np.random.randint(len(array)) - np.random.randint(len(array)) * m
    change = np.random.choice([-1, 1])
    for x in range(len(array)):
        for y in range(len(array[x])):
            if y >= m * x + b:
                array[x][y] += change
            else:
                array[x][y] -= change


# Loop to apply lines and print the % complete
i = 0
for i in range(FRACS):
    apply_line()
    print(f"{i/(FRACS) * 100}"[:4]+"%")

# Finding the highest value in the array after terrain has been created.
maximum = 0
for x in range(0, SIDE_LENGTH):
    for y in range(0, SIDE_LENGTH):
        maximum = max(array[x][y], maximum)


# Converting each point from a raw height value to a percentage of the maximum terrian
for x in range(0, SIDE_LENGTH):
    for y in range(0, SIDE_LENGTH):
        array[x][y] = int((array[x][y] / maximum) * 100)
        # Ensuring any value below the ocean line will be uniformly blue
        if array[x][y] < OCEAN_HEIGHT:
            array[x][y] = 0

# Plotting the resulting graph
plt.axis("off")
plt.imshow(array, cmap="terrain")
plt.show()
