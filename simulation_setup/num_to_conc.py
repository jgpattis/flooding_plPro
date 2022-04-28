# This script will turn a number of ligads into a concnetration given a box size

import sys, argparse
import numpy as np

def num_to_conc(num, gro):
    ''' This will turn a number of ligads into a concnetration given a box size
    num / (Na x box volume) = concentration
    
    inputs:
        num: int
            number of ligands
        gro: string of file name
            gro file with box vectors to determine box volume
    returns: float
    '''
    Na = 6.022149 * 10 ** 23 # avogadro's number
    with open(gro) as f:
        lines = f.readlines()
        last = lines[-1]

    x, y, z = [float(i) for i in last.split()]
    vol = x * y * z * 10 ** -24 # volume in L

    return np.round(num / (Na * vol), 4)

if __name__ == '__main__':
    usage = """ Usage: $ python num_to_conc.py [number of ligands] [file.gro]

    INPUTS
        number of ligands
        gro file

    OUTPUTs
        concentration

    EXAMPLE
        $ python num_to_conc.py 150 7cmd_box.gro

    """

    if len(sys.argv) != 3:
        print(usage)
        sys.exit(1)

    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=usage)
    parser.add_argument('num', type=int, help='the number of ligands')
    parser.add_argument('gro', type=str, help='the name of the gro file')

    args = parser.parse_args()

    num1 = args.num
    gro1 = args.gro

    out = num_to_conc(num1, gro1)
    print(f'The concentration is: {out}')

