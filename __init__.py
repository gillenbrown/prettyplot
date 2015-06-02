from palettable.tableau import Tableau_10
import matplotlib as mpl

from .tools import *
from .colors import *

mpl.rcParams['axes.color_cycle'] = [Tableau_10.hex_colors[1],
                                    Tableau_10.hex_colors[0]] + \
                                   Tableau_10.hex_colors[2:]
mpl.rcParams['legend.scatterpoints'] = 1
mpl.rcParams['savefig.format'] = 'pdf'
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'Helvetica'
mpl.rcParams['font.size'] = 14
mpl.rcParams['axes.labelsize'] = 14
mpl.rcParams['xtick.labelsize'] = 12
mpl.rcParams['ytick.labelsize'] = 12
mpl.rcParams['patch.edgecolor'] = almost_black
mpl.rcParams['text.color'] = almost_black
mpl.rcParams['axes.edgecolor'] = almost_black
mpl.rcParams['axes.labelcolor'] = almost_black
mpl.rcParams['xtick.color'] = almost_black
mpl.rcParams['ytick.color'] = almost_black
mpl.rcParams['grid.color'] = almost_black
