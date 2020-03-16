import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/antareep/codes/class_public-master/output/nl_z1_pk.dat', '/home/antareep/codes/class_public-master/output/nl_z1_pk_nl.dat', '/home/antareep/codes/class_public-master/output/nl_z2_pk.dat', '/home/antareep/codes/class_public-master/output/nl_z2_pk_nl.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['nl_z1_pk', 'nl_z1_pk_nl', 'nl_z2_pk', 'nl_z2_pk_nl']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'P(Mpc/h)^3']
tex_names = ['P (Mpc/h)^3']
x_axis = 'k (h/Mpc)'
ylim = []
xlim = [1e-05, 10.0]
ax.loglog(curve[:, 0], abs(curve[:, 1]))

index, curve = 1, data[1]
y_axis = [u'P(Mpc/h)^3']
tex_names = ['P (Mpc/h)^3']
x_axis = 'k (h/Mpc)'
ylim = []
xlim = [1e-05, 10.0]
ax.loglog(curve[:, 0], abs(curve[:, 1]))

index, curve = 2, data[2]
y_axis = [u'P(Mpc/h)^3']
tex_names = ['P (Mpc/h)^3']
x_axis = 'k (h/Mpc)'
ylim = []
xlim = [1e-05, 10.0]
ax.loglog(curve[:, 0], abs(curve[:, 1]))

index, curve = 3, data[3]
y_axis = [u'P(Mpc/h)^3']
tex_names = ['P (Mpc/h)^3']
x_axis = 'k (h/Mpc)'
ylim = []
xlim = [1e-05, 10.0]
ax.loglog(curve[:, 0], abs(curve[:, 1]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('k (h/Mpc)', fontsize=16)
ax.set_xlim(xlim)
ax.set_ylim()
plt.show()