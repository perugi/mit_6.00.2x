import numpy as np

data = [10, 4, 12, 15, 20, 5]
data = np.array(data)
cov = data.std() / data.mean()
print(cov)
