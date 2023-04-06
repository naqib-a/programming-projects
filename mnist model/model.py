import numpy as np
import random
import wandb
import matplotlib.pyplot as plt

train_x = np.load("train_inputs.npy")
train_y = np.load("train_outputs.npy")
test_x = np.load("test_inputs.npy")
test_y = np.load("test_outputs.npy")

p = train_x[random.randint(1,len(train_x))]
plt.imshow(p)
plt.show()
