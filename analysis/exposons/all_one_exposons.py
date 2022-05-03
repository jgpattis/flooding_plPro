import mdtraj as md
import numpy as np
import enspara.info_theory.exposons as exp
from enspara.info_theory.mutual_info import weighted_mi
from sklearn.cluster import AffinityPropagation

damping = 0.9
threshold = 0.06

sasa_list = [0] * 9
for i in range(9):
    sasa_list[i] = np.load(f'sasa_{i}.npy')

sasa_cat = np.concatenate(sasa_list)

gro = md.load('7OFS/10_milli_molar/analysis/frame0_nw.gro')
gro2 = gro.atom_slice(gro.top.select('protein'))

sasas = exp.condense_sidechain_sasas(sasa_cat, gro2.top)
weights = np.full((len(sasa_cat),), 1 / len(sasa_cat))

sasa_mi = weighted_mi(sasas > threshold, weights)
c = AffinityPropagation(damping=damping)
c.fit(sasa_mi)
sm, ex = exp.exposons_from_sasas(sasas, damping, weights, threshold)

np.save('sasa_mi_9_6_all9.npy', sm)

np.save('exposons_9_6_all9.npy', ex)
