import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/antareep/codes/class_public-master/output/try02_cl.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['try02_cl']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'EE', u'TE']
tex_names = ['EE', 'TE']
x_axis = 'l'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 2]))
ax.loglog(curve[:, 0], abs(curve[:, 3]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('$\ell$', fontsize=16)
plt.show()