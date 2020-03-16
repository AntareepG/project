import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/antareep/codes/class_public-master/output/axionfluid1_background.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['axionfluid1_background']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'w_ULAfld']
tex_names = [u'(8\\pi G/3)w_ULAfld']
x_axis = 'z'
ylim = []
xlim = []
ax.semilogx(curve[:, 0], curve[:, 13])

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('z', fontsize=16)
plt.show()