#!/usr/bin/env python

from DECIMER import predict_SMILES

image_path = "../input-images/1.png"
smiles = predict_SMILES(image_path)
print(smiles)

