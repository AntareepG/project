import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/antareep/codes/class_public-master/output/efluid_background.dat', '/home/antareep/codes/class_public-master/output/fluid_background.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['efluid_background', 'fluid_background']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'rho_cdm', u'rho_ur', u'rho_efld']
tex_names = [u'(8\\pi G/3)rho_cdm', u'(8\\pi G/3)rho_efld', u'(8\\pi G/3)rho_ur']
x_axis = 'proper time [Gyr]'
ylim = []
xlim = []
ax.loglog(curve[:, 1], abs(curve[:, 10]))
ax.loglog(curve[:, 1], abs(curve[:, 13]))
ax.loglog(curve[:, 1], abs(curve[:, 12]))

index, curve = 1, data[1]
y_axis = [u'rho_cdm', u'rho_ur', u'rho_fld', u'w_fld']
tex_names = [u'(8\\pi G/3)rho_cdm', u'(8\\pi G/3)rho_fld', u'(8\\pi G/3)w_fld', u'(8\\pi G/3)rho_ur']
x_axis = 'proper time [Gyr]'
ylim = []
xlim = []
ax.loglog(curve[:, 1], abs(curve[:, 10]))
ax.loglog(curve[:, 1], abs(curve[:, 14]))
ax.loglog(curve[:, 1], abs(curve[:, 12]))
ax.loglog(curve[:, 1], abs(curve[:, 13]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('proper time [Gyr]', fontsize=16)
plt.show()