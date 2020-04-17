import os
import pandas as pd
import autograd
from autograd.builtins import tuple
import autograd.numpy as np

from scipy.integrate import odeint as BlackBox
import matplotlib.pyplot as plt


location = "Miami-Dade"
population = 2717000
df = pd.read_csv(os.getcwd() + "/data/" + location + ".csv")
confirm = df["confirm_count"].values / population


def f(y, t ,theta):
    '''Function describing dynamics of the system'''
    
    S, I = y
    ds = - theta * S * I
    di = theta * S * I - I

    return np.array([ds, di])


#Jacobian wrt y
J = autograd.jacobian(f, argnum=0)
#Gradient wrt theta
grad_f_theta = autograd.jacobian(f, argnum=2)


def ODESYS(Y, t, theta):

    #Y will be length 4.
    #Y[0], Y[1] are the ODEs
    #Y[2], Y[3] are the sensitivities

    #ODE
    dy_dt = f(Y[0:2], t, theta)
    #Sensitivities
    grad_y_theta = J(Y[:2],t,theta)@Y[-2::] + grad_f_theta(Y[:2],t,theta)

    return np.concatenate([dy_dt,grad_y_theta])


def Cost(y_obs):
    def cost(Y):
        '''Squared Error Loss'''
        n = y_obs.shape[0]
        err = np.linalg.norm(y_obs - Y, 2, axis = 1)

        return np.sum(err)/n

    return cost


np.random.seed(123)

Y0 = np.array([(1 - confirm[0]), confirm[0], 0.0, 0.0])
#Space to compute solutions
t = np.linspace(0, 5, len(confirm))

ground_truth = np.array([1 - confirm, confirm]).reshape(-1, 2)

plt.scatter(t, 
            ground_truth[:,0],
            marker='.', alpha=0.5,
            label='ground truth S')
plt.scatter(t, 
            ground_truth[:,1], 
            marker='.', 
            alpha=0.5,
            label='ground truth I')

plt.legend()

i = 0
last_theta = 0
theta = 1.5
cost = Cost(ground_truth[:,:2])
grad_C = autograd.grad(cost)

maxiter = 10000
learning_rate = 1 #Big steps

while i < maxiter and abs(theta - last_theta) > 1e-10:
    i += 1
    last_theta = theta
    sol = BlackBox(ODESYS, y0=Y0, t=t, args=tuple([theta]))
    Y = sol[:,:2]
    
    theta -= learning_rate * (grad_C(Y) * sol[:, -2:]).sum()
    if i % 10 == 0:
        print(theta)
    

predict = BlackBox(ODESYS, y0 = Y0, t = t, args = tuple([theta]))
# true_sol = BlackBox(ODESYS, y0 = Y0, t = t, args = tuple([theta]))


plt.plot(t, predict[:, 0], label = 'Predicted S', color = 'C0', linewidth = 5)
plt.plot(t, predict[:, 1], label = 'Predicted I', color = 'C1', linewidth = 5)

plt.scatter(t, predict[:, 0], marker = '.', alpha = 0.5)
plt.scatter(t, predict[:, 1], marker = '.', alpha = 0.5)


# plt.plot(t,true_sol[:,0], label = 'Estimated ', color = 'k')
# plt.plot(t,true_sol[:,1], color = 'k')

plt.legend()