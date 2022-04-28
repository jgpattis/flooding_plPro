the flooding simulations were set up using the following protocol.   
the protocol used in this paper is provided in flooding_setup.sh (not a fully automated script)   
a semi-automated generic setup is provided with automated_setup.sh

1. Download charmm36m for gromacs http://mackerell.umaryland.edu/charmm_ff.shtml
2. Protonate protein with propka 3.4 pdb2pqr 3.3.3 
    - pdb2pqr30 --ff CHARMM --ffout CHARMM --pdb-output 7ofs_h.pdb 7ofs_prot.pdb 7ofs_h.pqr
3. Examine ZN coordinating CYS make sure they are deprotonated and change resname to CYM to keep them deprotonated. Zinc coordinated by 189, 192, 224, 226
4. Protonate small molecule with maestro and save as mol2
5. Convert protein pdb to gromacs format
    - Pdb2gmx protein only
7. Submit small molecule to paramchem https://cgenff.umaryland.edu/
8. Convert paramchem output to gromacs 
9. place protein in a box with a 1.0 nm buffer
    - Editconf -d 1.0
10. Use conc_to_num.py to convert your disired concentration to a number of ligands given a specific box volume
    - Conc_to_num 0.1 molar is 85 ligands 
11. insert small molecule with
    - gmx insert-molecules
12. solvate your system
13. Add 0.15 M ions to the system
14. Generate restraints for ligand with genrestr
15. run energy minimization
16. run NPT equilibration for 0.5 ns with position restraints
17. run NVT equilibration for 0.5 ns with position restraints
18. run production NVT simulations!
