import os

for i in range(200):
    os.system(f'dvc exp run --queue -S model.conv_units={i}')