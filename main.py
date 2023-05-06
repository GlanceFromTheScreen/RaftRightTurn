import numpy as np
from scipy.optimize import minimize, rosen, rosen_der, Bounds

# bounds = Bounds([0, -0.5], [1.0, 2.0])
#
# eq_cons = {'type': 'eq',
#              'fun': lambda x: np.array(1 - x[0] - 2*x[1]),
#              'jac': lambda x: [[-1, -2]]}
#
# ineq_cons = {'type': 'ineq',
#              'fun': lambda x: np.array(1 - x[0] - 2*x[1]),
#              'jac': lambda x: [[-1, -2]]}
#
# x0 = np.array([0.5, 0])
#
# res = minimize(rosen, x0, method='SLSQP', jac=rosen_der,
#                constraints=[ineq_cons], options={'ftol': 0.9, 'disp': True},
#                bounds=bounds)
#
# print(res)



