import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import pyarrow.parquet as pq

import jax
import jax.numpy as jnp
import functools as ft

data = pd.read_parquet('./datasets/Benign-Monday-no-metadata.parquet')

sns.set_style('whitegrid')
plt.figure(figsize=(10, 6))
sns.histplot(data['Flow Duration'], bins=50, kde=True)
plt.title('Flow Duration Distribution')
plt.show()