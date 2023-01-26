mport numpy as np

#  A random vector  is generated  of size 20 with float numbers between 1 and 20
vector = np.random.uniform(1, 20, 20)
print("\n Random Vector \n",vector)

# Reshape the array to 4 by 5
reshaped_vector = vector.reshape(4, 5)
print(" array after reshaping to (4,5) \n")
print(reshaped_vector)

# The  maximum value in each row is found
max_values = np.argmax(reshaped_vector, axis=1)

# The maximum value in each row is replaced with 0
reshaped_vector[np.arrange(reshaped_vector.shape[0]), max_values] = 0
print(" replacing the maximum value  with 0  \n")
print(reshaped_vector)