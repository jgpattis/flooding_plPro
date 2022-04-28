# This script will turn a ligand concentration into a number of ligads given a box size

import sys, argparse
import numpy as np

def conc_to_num(conc, gro):
    ''' This will turn a concnetration into a number of ligands given a box size
    conc x Na x box volume = number
    
    inputs:
        conc: float
            concentration in Molar
        gro: string of file name
            gro file with box vectors to determine box volume
    returns: int
    '''
    Na = 6.022149 * 10 ** 23 # avogadro's number
    with open(gro) as f:
        lines = f.readlines()
        last = lines[-1]

    x, y, z = [float(i) for i in last.split()]
    vol = x * y * z * 10 ** -24 # volume in L

    return np.round(conc * Na * vol, 0)

if __name__ == '__main__':
    usage = """ Usage: $ python num_to_conc.py [concentration] [file.gro]

    INPUTS
        conc            The concentration in Molar
        gro file

    OUTPUTs
        number of ligands

    EXAMPLE
        $ python num_to_conc.py 0.15 7cmd_box.gro

    """

    if len(sys.argv) != 3:
        print(usage)
        sys.exit(1)

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=usage)
    parser.add_argument('conc', type=float, help='The concentration in Molar')
    parser.add_argument('gro', type=str, help='the name of the gro file')

    args = parser.parse_args()

    conc1 = args.conc
    gro1 = args.gro

    out = conc_to_num(conc1, gro1)
    print(f'The number of ligands should be: {out}')

