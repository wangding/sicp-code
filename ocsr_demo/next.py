#!/usr/bin/env python

import torch
from MolNexTR import molnextr

image = '../input-images/1.png'
ckpt  = '../checkpoints/molnextr_best.pth'

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model  = molnextr(ckpt, device)
output = model.predict_final_results(image, return_atoms_bonds=False)

print(output['predicted_smiles'])
print(output['predicted_molfile'])
