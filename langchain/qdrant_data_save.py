
KEY = 'sk-proj-XJYwiH1QviHBnPLIkBcIT3BlbkFJ83Zm052mWPdCedSL3E69'
from langchain_openai import ChatOpenAI
import sys
__import__('pysqlite3')
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import chromadb
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

qdrant_client = QdrantClient(host='localhost', port=6333)
qdrant_client.recreate_collection(
    collection_name='startups',
    vectors_config=VectorParams(size=384, distance=Distance.COSINE),
)
import numpy as np
import json

fd = open('../startups_demo.json')

# payload is now an iterator over startup data_gmt
payload = map(json.loads, fd)

# Here we load all vectors into memory, numpy array works as iterable for itself.
# Other option would be to use Mmap, if we don't want to load all data_gmt into RAM
vectors = np.load('../vectors.npy')

qdrant_client.upload_collection(
    collection_name='startups',
    vectors=vectors,
    payload=payload,
    ids=None,  # Vector ids will be assigned automatically
    batch_size=256  # How many vectors will be uploaded in a single request?
)
def check_data():
    llm = ChatOpenAI(api_key=KEY)
    # llm.invoke("how can langsmith help with testing?")
    # chroma_client = chromadb.Client()
    # collection = chroma_client.create_collection(name="my_collection")

    # qdrant_client.recreate_collection(
    #     collection_name='startups',
    #     vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    # )

if __name__ == '__main__':
    check_data()