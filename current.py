import numpy as nx

charge=2
omega=7.1e-6
appliedPotential=-0.25
temperature=298.
gasConstant=8.314
faradaysConstant=9.6485e4
alpha = 0.4
i0 = 40.
kPlus=150.
kMinus=2.45e7
bulkSuppressor=.02

Fbar = faradaysConstant / gasConstant / temperature
potential = -appliedPotential * 0.1
cbar = 0.6
current0 = i0 * (nx.exp(alpha * Fbar * potential) - nx.exp(-(2 - alpha) * Fbar * potential)) * cbar

v0 = current0 * omega / charge / faradaysConstant

print kPlus * bulkSuppressor / kMinus/ v0
