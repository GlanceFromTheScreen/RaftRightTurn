import numpy as np
from scipy.optimize import minimize
from scipy.optimize import rosen, rosen_der, rosen_hess, rosen_hess_prod
from scipy.optimize import Bounds


bounds = Bounds([-1.0, -1.0], [1.0, 1.0])


def fun(x):
    """The Rosenbrock function"""
    return x[0] ** 2 + x[1] ** 2


ineq_cons = {'type': 'ineq',
             'fun': lambda x: np.array([1 - x[0] - 2 * x[1],
                                          1 - x [0] ** 2 - x [1],
                                          1 - x [0] ** 2 + x [1]]),
             'jac': lambda x: np.array ([[- 1.0, -2.0],
                                          [-2 * x [0], -1.0],
                                          [-2 * x [0], 1.0]])
            }

eq_cons = {'type': 'eq',
           'fun': lambda x: np.array ([2 * x [0] + x [1] - 1]),
           'jac': lambda x: np.array ([2.0, 1.0])
          }


x0 = np.array([0.5, 0])
res = minimize(fun, x0, method='SLSQP', jac=lambda x: [2*x[0], 2*x[1]],
               constraints=[eq_cons, ineq_cons], options={'ftol': 1e-9, 'disp': True},
               bounds=bounds)

print(res.x)


