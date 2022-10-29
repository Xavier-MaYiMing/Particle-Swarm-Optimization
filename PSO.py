#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/9/1 11:41
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : PSO.py
# @Statement : Particle Swarm Optimization
# @Reference : Kennedy J, Eberhart R. Particle swarm optimization[C]//Proceedings of ICNN'95-International Conference on Neural Networks. IEEE, 1995, 4: 1942-1948.
import random
import math
import matplotlib.pyplot as plt


def obj(x):
    """
    The objective function of pressure vessel design
    :param x:
    :return:
    """
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    g1 = -x1 + 0.0193 * x3
    g2 = -x2 + 0.00954 * x3
    g3 = -math.pi * x3 ** 2 - 4 * math.pi * x3 ** 3 / 3 + 1296000
    g4 = x4 - 240
    if g1 <= 0 and g2 <= 0 and g3 <= 0 and g4 <= 0:
        return 0.6224 * x1 * x3 * x4 + 1.7781 * x2 * x3 ** 2 + 3.1661 * x1 ** 2 * x4 + 19.84 * x1 ** 2 * x3
    else:
        return 1e10


def boundary_check(value, l_bound, u_bound):
    """
    The boundary check
    :param value:
    :param l_bound: lower bound
    :param u_bound: upper bound
    :return:
    """
    for i in range(len(value)):
        value[i] = max(value[i], l_bound[i])
        value[i] = min(value[i], u_bound[i])
    return value


def main(pop, iter, vmin, vmax):
    """
    The main function of the PSO
    :param pop: the population size
    :param iter: the iteration number
    :param vmin: the minimum velocity (list)
    :param vmax: the maximum velocity (list)
    :return:
    """
    # Step 1. Parameter settings
    # Reference: Trelea I C. The particle swarm optimization algorithm: convergence analysis and parameter selection[J]. Information Processing Letters, 2003, 85(6): 317-325.
    # V(t+1) = \omega * V(t)+\phi_1 * r_1 * (p(t) - x(t)) + \phi_2 * r_2 * (g(t) - x(t))
    # p(t): personal best; g(t): global best
    # r_1, r_2: two random numbers uniformly distributed in [0, 1]
    omega = 0.6  # inertia weight to control the influence of the previous velocity value on the updated velocity
    phi1 = 1.7  # cognitive weight
    phi2 = 1.7  # social weight
    dim = len(vmin)  # dimension
    u_bound = [100, 100, 100, 100]  # upper bound
    l_bound = [0, 0, 10, 10]  # lower bound

    # Step 2. Initialization
    fitness = []
    position = []
    velocity = []
    for i in range(pop):
        temp_position = [random.uniform(l_bound[j], u_bound[j]) for j in range(dim)]
        position.append(temp_position)
        velocity.append([random.uniform(vmin[j], vmax[j]) for j in range(dim)])
        fitness.append(obj(temp_position))
    g_best = min(fitness)  # global best
    p_best = fitness.copy()
    g_best_location = position[fitness.index(g_best)]  # the particle location of global best
    p_best_location = position.copy()  # the particle location of personal best
    iter_best = [g_best]

    # Step 3. The main loop
    for iteration in range(iter):
        for i in range(pop):
            r1 = random.random()
            r2 = random.random()
            velocity[i] = [omega * velocity[i][j] + phi1 * r1 * (p_best_location[i][j] - position[i][j]) + phi2 * r2 * (g_best_location[j] - position[i][j]) for j in range(dim)]
            velocity[i] = boundary_check(velocity[i], vmin, vmax)
            position[i] = [position[i][j] + velocity[i][j] for j in range(dim)]
            position[i] = boundary_check(position[i], l_bound, u_bound)
            new_fitness = obj(position[i])
            if new_fitness < p_best[i]:
                p_best[i] = new_fitness
                p_best_location[i] = position[i].copy()
                if new_fitness < g_best:
                    g_best = new_fitness
                    g_best_location = position[i].copy()
        iter_best.append(g_best)

    # Step 4. Sort the results
    x = [i for i in range(iter + 1)]
    plt.figure()
    plt.plot(x, iter_best, linewidth=2, color='blue')
    plt.xlabel('Iteration number')
    plt.ylabel('Global optimal value')
    plt.title('Convergence curve')
    plt.ticklabel_format(style='sci', scilimits=(0, 0))
    plt.show()
    return {'best solution': g_best_location, 'best score': g_best}


if __name__ == '__main__':
    pop = 50
    iter = 500
    vmin = [-2, -2, -2, -2]
    vmax = [2, 2, 2, 2]
    print(main(pop, iter, vmin, vmax))
