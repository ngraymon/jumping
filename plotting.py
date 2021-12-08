
# system imports
import os
from os.path import join

# third party imports
import torch
import numpy as np

import matplotlib as mpl
# `use_backend` needed if no x-server is available
mpl.use(['pdf', 'Agg', 'svg'][1])
from matplotlib import pyplot as plt

# local imports
from flags import flags


def plot_helium(network):
    """ Plot the helium wavefunction over a range of electron positions """
    plt.rcParams['text.usetex'] = True
    n_step_plot = flags.n_step_plot
    plot_path = flags.plot_path

    # fix the first electron for the Helium atom and vary the second
    # (0.5,0,0) a_0
    # (x,0,0) a_0, with x=linespace(-1,1,20)
    # (0.5 cosθ,0.5 sinθ,0)a_0

    linear = np.array([
        [[0.5, 0, 0], [x, 0, 0]]
        for x in np.linspace(-1, 1, n_step_plot)
    ])
    rotational = np.array([
        [[0.5, 0, 0], [0.5*np.cos(theta), 0.5*np.sin(theta), 0]]
        for theta in np.linspace(-180, 180, n_step_plot)
    ])

    phi_lin = network.forward(torch.tensor(linear))
    phi_rot = network.forward(torch.tensor(rotational))

    fig, ax = plt.subplots(2)
    fig.suptitle('Wave function for helium atom')
    fig.tight_layout()

    # Make your plot, set your axes labels
    ax[0].plot(torch.linspace(-1, 1, 10), phi_lin)
    ax[0].set_xlabel('x [Bohr]')
    ax[0].set_ylabel(r' $\psi$')

    # Turn off tick labels
    ax[0].set_yticklabels([])

    ax[1].plot(torch.deg2rad(torch.linspace(-180, 180, 10)), phi_rot)
    ax[1].set_xlabel(r'$\theta$')
    ax[1].set_ylabel(r' $\psi$')
    ax[1].set_yticklabels([])

    strFile = join(plot_path, 'Wavefunction.png')

    # overwrite the previous file
    if os.path.isfile(strFile):
        os.remove(strFile)

    plt.savefig(strFile)


def plot_loss(losstot):
    """ Plot the loss per epoch """

    plt.rcParams['text.usetex'] = True
    plot_path = flags.plot_path

    plt.plot(losstot)
    plt.xlabel('Epoch')
    plt.ylabel('Local Energy (loss) [J]')

    strFile = join(plot_path, 'Local_Energy.png')

    # overwrite the previous file
    if os.path.isfile(strFile):
        os.remove(strFile)

    plt.savefig(strFile)