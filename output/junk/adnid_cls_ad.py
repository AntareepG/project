import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/antareep/codes/class_public-master/output/adnid_cls_ad.dat', '/home/antareep/codes/class_public-master/output/adnid_cls_nid.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['adnid_cls_ad', 'adnid_cls_nid']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax.semilogx(curve[:, 0], curve[:, 1])

index, curve = 1, data[1]
y_axis = [u'TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax.semilogx(curve[:, 0], curve[:, 1])

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('$\ell$', fontsize=16)
plt.show()