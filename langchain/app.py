from sentence_transformers import SentenceTransformer

KEY = 'sk-proj-XJYwiH1QviHBnPLIkBcIT3BlbkFJ83Zm052mWPdCedSL3E69'
from langchain_openai import ChatOpenAI
from qdrant_client import QdrantClient


class NeuralSearcher:

    def __init__(self, collection_name):
        self.collection_name = collection_name
        # Initialize encoder model
        self.model = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')
        # initialize Qdrant client
        self.qdrant_client = QdrantClient(host='localhost', port=6333)

    def search(self, text: str):
        # Convert text query into vector
        vector = self.model.encode(text).tolist()

        # Use `vector` for search for closest vectors in the collection
        search_result = self.qdrant_client.search(
            collection_name=self.collection_name,
            query_vector=vector,
            query_filter=None,  # We don't want any filters for now
            # top=5  # 5 the most closest results is enough
        )
        # `search_result` contains found vector ids with similarity scores along with the stored payload
        # In this function we are interested in payload only
        payloads = [hit.payload for hit in search_result]
        return payloads


from qdrant_client.models import Filter

city_of_interest = "Berlin"

# Define a filter for cities
# city_filter = Filter({
#     "must": [{
#         "key": "city", # We store city information in a field of the same name
#         "match": { # This condition checks if payload field have requested value
#             "keyword": city_of_interest
#         }
#     }]
# })

# search_result = NeuralSearcher(collection_name='startups')
# res = search_result.search(text='syllabus for twelfth')
# print(res)


def check_data():
    # pass
    llm = ChatOpenAI(api_key=KEY)
    print(llm)


if __name__ == '__main__':
    check_data()
