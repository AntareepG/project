import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/antareep/codes/class_public-master/output/st_cl.dat', '/home/antareep/codes/class_public-master/output/st_cl_lensed.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['st_cl', 'st_cl_lensed']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'BB']
tex_names = ['BB']
x_axis = 'l'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 4]))

index, curve = 1, data[1]
y_axis = [u'BB']
tex_names = ['BB']
x_axis = 'l'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 4]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('$\ell$', fontsize=16)
plt.show()