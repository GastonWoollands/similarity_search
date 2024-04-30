# Similarity Search Function

This repository contains a Python function named `similarity_search` that performs a semantic search on a list of query texts against a list of known texts using a given model.

## Function Overview

The `similarity_search` function takes four required parameters:

- `text_q`: A list of query texts to be searched.
- `texts_k`: A list of known texts against which the query texts are searched.
- `model`: A model used to encode the texts.
- `top_k`: The number of top similar texts to return for each query text (default is 3).
- `score`: The minimum score required for a text to be included in the results (default is 0).

The function returns a dictionary where each key is a query text and the value is a dictionary containing the top similar texts from the known texts and their corresponding similarity scores.

## Usage

You can use the `similarity_search` function by calling it with the required parameters. For example:

```python
from similarity_search import similarity_search
from sentence_transformers import SentenceTransformer

query_texts = ["text1", "text2", "text3"]
known_texts = ["text1a", "text1b", "text2a", "text2b", "text3a", "text3b"]
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

results = similarity_search(query_texts, known_texts, model, top_k=1, score=0.5)


You can then access the results dictionary to see the top similar texts for each query text:
print(results["text1"])  # Output: {"text1a"  {"text1b": 0.6}
print(results["text2"])  # Output: {"text2a"  {"text2b": 0.7}
print(results["text3"])  # Output: {"text3a"  {"text3b": 0.6}

```

# Instalation

To use the similarity_search function, you will need to install PyTorch and your chosen model. You can do this using pip:
pip install sentence-transformers

# License

This repository is licensed under the MIT License. See the LICENSE file for details.
