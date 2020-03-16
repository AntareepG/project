import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/antareep/codes/class_public-master/output/axionpert1_background.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['axionpert1_background']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'rho_ULAfld']
tex_names = [u'(8\\pi G/3)rho_ULAfld']
x_axis = 'z'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 12]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('z', fontsize=16)
plt.show()