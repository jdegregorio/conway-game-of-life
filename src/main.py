# External imports
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import animation

# Internal imports
import sys
from pyhere import here
sys.path.append(here('src'))
from src.conway import Conway


def init():
    im.set_data(conway.env)
    return [im]


def animate(i):
    conway.step_frame()
    im.set_array(conway.env)
    return [im]


if __name__ == "__main__":

    # Initialize game of life
    conway = Conway(size=100, seed_pct=0.05)
    conway.seed_env()

    # Animate simulation
    fig = plt.figure(figsize=(10, 10))
    im = plt.imshow(
        conway.env,
        alpha=0.5, cmap=colors.ListedColormap(["white", "darkgreen"])
    )
    anim = animation.FuncAnimation(
        fig, animate, init_func=init, frames=100, interval=20, blit=True
    )
    writergif = animation.PillowWriter(fps=5)
    anim.save('animation.gif', writer=writergif)
