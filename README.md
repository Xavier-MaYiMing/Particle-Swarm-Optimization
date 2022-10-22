### Particle Swarm Optimization

##### Reference: Kennedy J, Eberhart R. Particle swarm optimization[C]//Proceedings of ICNN'95-International Conference on Neural Networks. IEEE, 1995, 4: 1942-1948.

| Variables       | Meaning                                                      |
| --------------- | ------------------------------------------------------------ |
| pop             | The number of population                                     |
| u_bound         | List, the upper bound of the i-th dimension is u_bound[i]    |
| l_bound         | List, the lower bound of the i-th dimension is l_bound[i]    |
| vmin            | List, the minimum velocity of the particle on the i-th dimension is vmin[i] |
| vmax            | List, the maximum velocity of the particle on the i-th dimension is vmax[i] |
| iter            | The maximum number of iterations                             |
| omega           | The inertia weight to control the influence of the previous velocity value on the updated velocity |
| phi1            | The cognitive weight                                         |
| phi2            | The social weight                                            |
| dim             | The number of dimensions                                     |
| position        | List, the position of the i-th particle is position[i]       |
| fitness         | List, the score of the i-th particle is fitness[i]           |
| velocity        | List, the velocity of the i-th particle is velocity[i]       |
| g_best          | The global best score                                        |
| g_best_location | The global best position                                     |
| p_best          | List, the personal best score of the i-th particle is p_best[i] |
| p_best_location | List, the personal best position of the i-th particle is p_best[i] |
| iter_best       | List, the best so-far score of each iteration                |

#### Test problem: Pressure vessel design

![](https://github.com/Xavier-MaYiMing/Particle-Swarm-Optimization/blob/main/Pressure%20vessel%20design.png)

$$
\begin{align}
&\text{min}\ f(x)=0.6224x_1x_3x_4+1.7781x_2x_3^2+3.1661x_1^2x_4+19.84x_1^2x_3,\\
&\text{s.t.} \\
&-x_1+0.0193x_3\leq0,\\
&-x_3+0.0095x_3\leq0,\\
&-\pi x_3^2x_4-\frac{4}{3}\pi x_3^3+1296000\leq0,\\
&x_4-240\leq0,\\
&0\leq x_1\leq99,\\
&0\leq x_2 \leq99,\\
&10\leq x_3 \leq 200,\\
&10\leq x_4 \leq 200.
\end{align}
$$


#### Example

```python
if __name__ == '__main__':
    pop = 50
    iter = 500
    vmin = [-2, -2, -2, -2]
    vmax = [2, 2, 2, 2]
    print(main(pop, iter, vmin, vmax))
```

##### Output:

![](https://github.com/Xavier-MaYiMing/Particle-Swarm-Optimization/blob/main/convergence%20curve.png)

```python
{
    'best solution': [1.300568607387978, 0.6431938035005514, 67.38697386901593, 10.0], 
    'best score': 8053.847210456193,
}
```

