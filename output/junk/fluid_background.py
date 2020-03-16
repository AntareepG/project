import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/home/antareep/codes/class_public-master/output/fluid_background.dat', '/home/antareep/codes/class_public-master/output/axionfluid_background.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['fluid_background', 'axionfluid_background']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'rho_cdm', u'rho_fld', u'w_fld', u'rho_lambda']
tex_names = [u'(8\\pi G/3)rho_cdm', u'(8\\pi G/3)rho_lambda', u'(8\\pi G/3)rho_fld', u'(8\\pi G/3)w_fld']
x_axis = 'proper time [Gyr]'
ylim = []
xlim = []
ax.loglog(curve[:, 1], abs(curve[:, 10]))
ax.loglog(curve[:, 1], abs(curve[:, 12]))
ax.loglog(curve[:, 1], abs(curve[:, 13]))
ax.loglog(curve[:, 1], abs(curve[:, 11]))

index, curve = 1, data[1]
y_axis = [u'rho_cdm', u'rho_ULAfld', u'w_ULAfld', u'rho_lambda']
tex_names = [u'(8\\pi G/3)rho_cdm', u'(8\\pi G/3)rho_lambda', u'(8\\pi G/3)rho_ULAfld', u'(8\\pi G/3)w_ULAfld']
x_axis = 'proper time [Gyr]'
ylim = []
xlim = []
ax.loglog(curve[:, 1], abs(curve[:, 10]))
ax.loglog(curve[:, 1], abs(curve[:, 12]))
ax.loglog(curve[:, 1], abs(curve[:, 13]))
ax.loglog(curve[:, 1], abs(curve[:, 11]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('proper time [Gyr]', fontsize=16)
plt.show()