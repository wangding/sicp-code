#!/usr/bin/env python

import torch
from molscribe import MolScribe

image = '../input-images/1.png'
ckpt  = '../checkpoints/swin_base_char_aux_1m.pth'

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model  = MolScribe(ckpt, device)
output = model.predict_image_file(image, return_atoms_bonds=False, return_confidence=False)

print(output['smiles'])
print(output['molfile'])
