import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/antareep/codes/class_public-master/output/try00_background.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['try00_background']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'rho_g', u'rho_cdm']
tex_names = [u'(8\\pi G/3)rho_g', u'(8\\pi G/3)rho_cdm']
x_axis = 'z'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 8]))
ax.loglog(curve[:, 0], abs(curve[:, 10]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('z', fontsize=16)
plt.show()
fig.savefig('output/background.pdf')