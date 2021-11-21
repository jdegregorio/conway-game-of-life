# Conway's Game of Life Simulation
A simulation of Conway's Game of Life

## Rules

From Wikipedia [LINK](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

> The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead, (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. 
> 
> At each step in time, the following transitions occur:
>  * Any live cell with fewer than two live neighbours dies, as if by underpopulation.
>  * Any live cell with two or three live neighbours lives on to the next generation.
>  * Any live cell with more than three live neighbours dies, as if by overpopulation.
>  * Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
> 
> These rules, which compare the behavior of the automaton to real life, can be condensed into the following:
>  * Any live cell with two or three live neighbours survives.
>  * Any dead cell with three live neighbours becomes a live cell.
>  * All other live cells die in the next generation. Similarly, all other dead cells stay dead.
> 
> The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed, live or dead; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a tick. Each generation is a pure function of the preceding one. The rules continue to be applied repeatedly to create further generations.

## Project Description

### Overview

```
Conway's Game of Life Demonstration
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── animation.gif
└── src
    ├── __pycache__
    │   └── conway.cpython-38.pyc
    ├── conway.py
    ├── dev.py
    └── main.py
```

### conway.py

A high level class definition of the Conway Game of Life. The class includes methods for the following:
 * Initiate an object with specified grid size
 * Advanced the game one time step (implementation of game of life rules)
 * Simulate the game of life through multiple time steps


### main.py

An example demonstration of the game:
 * Create an instance
 * Simulate the game for n steps
 * Animate using matplotlib

