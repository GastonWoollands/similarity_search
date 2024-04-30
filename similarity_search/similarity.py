from sentence_transformers import SentenceTransformer
from sentence_transformers.util import semantic_search
from typing import List

def similarity_search(texts_q: List[str], texts_k: List[str], model, top_k = 3, score= 0):
    """
    Performs a semantic search on a list of query texts against a list of known texts using a given model.

    Args:
        text_q (List[str]): A list of query texts to be searched.
        texts_k (List[str]): A list of known texts against which the query texts are searched.
        model: A model used to encode the texts.
        top_k (int, optional): The number of top similar texts to return for each query text. Defaults to 3.
        score (int, optional): The minimum score required for a text to be included in the results. Defaults to 0.

    Returns:
        dict: A dictionary where each key is a query text and the value is a dictionary containing the top similar texts from the known texts and their corresponding similarity scores.
    """

    query = texts_q
    keys  = texts_k

    response_dict = {}

    embeddings_q = model.encode(query)
    embeddings_k = model.encode(keys)

    search = semantic_search(embeddings_q, embeddings_k, top_k=top_k)

    for j in range(len(search)):
        response_dict[query[j]] = {}
        sorted_results = []

        for i in range (0, top_k):
            if search[j][i].get('score') >= score:
                sorted_results.append((keys[search[j][i].get('corpus_id')], search[j][i].get('score')))
            else:
                pass
       
        sorted_results = sorted(sorted_results, key=lambda x: x[1], reverse=True)

        for result in sorted_results:
            response_dict[query[j]][result[0]] = result[1]
       
        response_dict[query[j]] = {k: response_dict[query[j]][k] for k, v in sorted_results}
   
    return response_dict