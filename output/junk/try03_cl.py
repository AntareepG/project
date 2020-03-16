import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/antareep/codes/class_public-master/output/try03_cl.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['try03_cl']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'EE', u'TE', u'Ephi']
tex_names = ['EE', 'TE', 'Ephi']
x_axis = 'l'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 2]))
ax.loglog(curve[:, 0], abs(curve[:, 3]))
ax.loglog(curve[:, 0], abs(curve[:, 7]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('$\ell$', fontsize=16)
plt.show()
fig.savefig('output/try.pdf')