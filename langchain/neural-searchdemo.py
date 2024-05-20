from sentence_transformers import SentenceTransformer
import numpy as np
import json
import pandas as pd
from tqdm.notebook import tqdm

# This code will download and create a pre-trained sentence encoder

# all-MiniLM-L6-v2 - is a distilated (lightweight) version of MPNet model.
# It is optimized for the fast inference.
# Full list of available models could be found here https://www.sbert.net/docs/pretrained_models.html
model = SentenceTransformer('all-MiniLM-L6-v2')
df = pd.read_json('../startups_demo.json', lines=True)
# Here we encode all startup descriptions
# We do encoding in batches, as this reduces overhead costs and significantly speeds up the process
vectors = model.encode([
    row.alt + ". " + row.description
    for row in df.itertuples()
], show_progress_bar=True)

# Now we have all our descriptions converted into vectors.
# We have 40474 vectors of 384 dimentions. The output layer of the model has this dimension
vectors.shape

# You can download this saved vectors and continue with rest part of the tutorial.
np.save('../vectors.npy', vectors, allow_pickle=False)