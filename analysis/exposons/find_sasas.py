import mdtraj as md
import numpy as np
import enspara.info_theory.exposons as exp

frame = md.load('7OFS/10_milli_molar/analysis/frame0_nw.gro')
prot = frame.top.select('protein')

traj_names = ['7OFS/10_milli_molar/analysis/plpro_yrl_10_whole_wrap.trr', '7OFS/50_milli_molar/analysis/plpro_yrl_50_whole_wrap.trr', '7OFS/100_milli_molar/analysis/plpro_yrl_100_whole_wrap.trr', 
                 '7oft/10_mm/analysis/7oft_10mm_whole_wrap.trr', '7oft/50_mm/analysis/7oft_50mm_whole_wrap.trr', '7oft/100_mm/analysis/7oft_100mm_whole_wrap.trr',
                 '7ofu/10_mm/analysis/7ofu_10mm_whole_wrap.trr', '7ofu/50_mm/analysis/7ofu_50mm_whole_wrap.trr', '7ofu/100_mm/analysis/7ofu_100mm_whole_wrap.trr']

#traj_names = ['10_milli_molar/analysis/plpro_yrl_10_whole.xtc', '50_milli_molar/analysis/plpro_yrl_50_whole.xtc', '100_milli_molar/analysis/plpro_yrl_100_whole.xtc']

for i, j in enumerate(traj_names):
    traj = md.load(j, top='7OFS/10_milli_molar/analysis/frame0_nw.gro', atom_indices=prot)
    sasa = md.shrake_rupley(traj, probe_radius=0.28)
    np.save(f'sasa_{i}.npy', sasa)


