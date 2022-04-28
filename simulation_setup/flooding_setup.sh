# steps to set up system

pdb2pqr30 --ff CHARMM --ffout CHARMM --pdb-output 7ofs_h.pdb 7ofs_prot.pdb 7ofs_h.pqr
# can also convert pqr back to pdb with chimera
# delete gamma hydrogen on CYS 189, 192, 224, and 226
# change resname from CYS to CYM for neutral cystine
gmx pdb2gmx -f 7ofs_h.pdb -o 7ofs_pqr.gro
# choose charmm36 ff and charmm tip3p water
# use epic in protein prep wizard to protonate ligand
# save as mol2
# submit mol2 to paramchem https://cgenff.umaryland.edu/
python cgenff_charmm2gmx_py3_nx2.py yrl yrl.mol2 yrl.str ~/Downloads/charmm36-jul2021.ff
gmx editconf -f 7ofs_pqr.gro -o 7ofs_box.gro -c -d 1.0 -bt cubic
gmx insert-molecules -f 7ofs_box.gro -ci yrl_ini.pdb -nmol 89 -o 100_milli_molar/7ofs_89_yrl.gro
# add prm, itp, and molecules line to top
gmx genrestr -f ../yrl_ini.pdb -o posre_yrl.itp
# add ifdef posres statement to bottem of small molecule itp
gmx solvate -cp 7ofs_89_yrl.gro -cs spc216.gro -o 7ofs_89_solv.gro -p topol.top 
gmx grompp -f ../../try3_pqr/ions.mdp -c 7ofs_89_solv.gro -p topol.top -o ions.tpr
gmx genion -s ions.tpr -o 7ofs_89_solv_ions.gro -p topol.top -pname SOD -nname CLA -neutral -conc 0.15
# select SOL for replacement
gmx grompp -f ../../try3_pqr/min_charmmgui.mdp -c 7ofs_89_solv_ions.gro -r 7ofs_89_solv_ions.gro -p topol.top -o em.tpr
gmx mdrun -s em.tpr -v -deffnm em
gmx grompp -f ../../try3_pqr/npt_charmmgui.mdp -c em.gro -r em.gro -p topol.top -o npt.tpr
gmx mdrun -s npt.tpr -v -deffnm npt
gmx grompp -f ../../try3_pqr/nvt_charmmgui.mdp -c npt.gro -r npt.gro -p topol.top -o nvt.tpr
gmx mdrun -s nvt.tpr -v -deffnm nvt
