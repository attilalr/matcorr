import numpy as np
from matcorr import mcorr

n = 10 # n random vectors
size = 10 # size of each vector

obj = mcorr()

for i in range(n):
  # add col method accept a name and a vector each time is called
  obj.add_col(str(i), np.random.random(size))

obj.show_matrix()
obj.writefig('mcorr.png')

# mcorr accept sns.heatmap keywords arguments

obj = mcorr(annot=False, cmap='hot', cbar=False, vmin=0.1, vmax=0.9)

for i in range(n):
  obj.add_col(str(i), np.random.random(size))

obj.show_matrix()
obj.writefig('mcorr2.png')


