#!/usr/bin/env python

import tensorflow as tf

print("TF Version:", tf.__version__)
print("GPU Support:", bool(tf.config.list_physical_devices('GPU')))
