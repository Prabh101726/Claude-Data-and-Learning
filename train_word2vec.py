# LESSON: Training Word2Vec on Custom Text
#
# So far you have USED a pretrained GloVe model someone else trained on Wikipedia.
# That is not enough. You need to know what actually happens during training.
#
# Today you will:
#   1. Build a small corpus (sentences) and preprocess it
#   2. Train a Word2Vec model from scratch using gensim — BOTH skip-gram and CBOW
#   3. Inspect what the model learned: similarity, most_similar, analogies
#   4. Visualize the learned embedding space in 2D using PCA + matplotlib
#
# BEFORE YOU WRITE ANY CODE — answer these three questions in comments below:
#   Q1. What is the difference between skip-gram (sg=1) and CBOW (sg=0)?
#       Which one tends to work better on small corpora, and why?
#   Q2. What does the `window` parameter control in Word2Vec training?
#   Q3. Why do we need PCA to visualize embeddings?
#
# Write your answers here:
# A1: TODO
# A2: TODO
# A3: TODO
#
# If you cannot answer those without looking them up, go back to sklearn.metrics.py
# and the Word2Vec theory. There is no point training a model you do not understand.
# ---------------------------------------------------------------------------

import gensim
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np

# ---------------------------------------------------------------------------
# STEP 1: Define your corpus
#
# A corpus is a list of sentences, where each sentence is a list of tokens.
# This corpus is intentionally small so training is fast — but it is large
# enough to see meaningful patterns if the sentences are coherent.
#
# TASK: Add at least 10 more sentences to this corpus.
# The more thematic overlap between sentences, the better the embeddings.
# Pick a theme: sports, cooking, technology, science — your choice.
# Do NOT just copy random sentences. They must share vocabulary.
# ---------------------------------------------------------------------------

corpus = [
    ["the", "cat", "sat", "on", "the", "mat"],
    ["the", "dog", "ran", "across", "the", "field"],
    ["cats", "and", "dogs", "are", "common", "pets"],
    ["the", "cat", "chased", "the", "mouse"],
    ["dogs", "love", "to", "run", "and", "play"],
    ["the", "mouse", "hid", "under", "the", "mat"],
    ["cats", "sleep", "on", "soft", "surfaces"],
    ["dogs", "fetch", "balls", "in", "the", "field"],
    # TODO: Add at least 10 more sentences here.
    # They should be tokenized (list of lowercase strings, no punctuation).
]

# ---------------------------------------------------------------------------
# STEP 2: Train TWO models — skip-gram and CBOW
#
# Parameters to use:
#   vector_size = 50   (embedding dimensions)
#   window      = 3    (context window size)
#   min_count   = 1    (include words that appear at least once)
#   epochs      = 200  (small corpus needs more passes)
#   sg          = 1    (1 = skip-gram, 0 = CBOW)
#
# TASK: Train both models. Call them `skipgram_model` and `cbow_model`.
# ---------------------------------------------------------------------------

# TODO: Train skipgram_model here

# TODO: Train cbow_model here


# ---------------------------------------------------------------------------
# STEP 3: Inspect what the models learned
#
# TASK: For BOTH models, print:
#   a) The 5 most similar words to "cat"
#   b) The 5 most similar words to "dog"
#   c) Cosine similarity between "cat" and "dog"
#   d) Cosine similarity between "cat" and "mat"
#
# Then answer in a comment: which model gave more meaningful results, and why?
# ---------------------------------------------------------------------------

# TODO: Print inspection results for skipgram_model

# TODO: Print inspection results for cbow_model

# Your observation:
# OBSERVATION: TODO


# ---------------------------------------------------------------------------
# STEP 4: Visualize the embedding space with PCA
#
# Choose 10-15 words from your corpus that you expect to cluster meaningfully.
# Extract their vectors, reduce to 2D with PCA, and plot them with labels.
#
# TASK: Complete the visualization function below.
# ---------------------------------------------------------------------------

def plot_embeddings(model, words, title):
    """
    Reduce word vectors to 2D using PCA and plot with word labels.

    Args:
        model: trained gensim Word2Vec model
        words: list of words to plot (must exist in model vocabulary)
        title: string title for the plot
    """
    # TODO: Filter out any words not in model.wv.key_to_index
    # TODO: Extract vectors for each valid word using model.wv[word]
    # TODO: Stack vectors into a 2D numpy array
    # TODO: Apply PCA(n_components=2) and transform
    # TODO: Scatter plot — each point labeled with its word
    # TODO: Set title, show grid, call plt.show()
    pass


words_to_plot = ["cat", "dog", "mouse", "mat", "field", "run", "play", "sleep"]
# TODO: Add more words from your expanded corpus

plot_embeddings(skipgram_model, words_to_plot, "Skip-gram Embeddings (PCA)")
plot_embeddings(cbow_model, words_to_plot, "CBOW Embeddings (PCA)")


# ---------------------------------------------------------------------------
# STEP 5: Reflection (write your answers as comments)
#
# R1. With only ~18 sentences, the embeddings are noisy. What would happen to
#     embedding quality if you trained on 1 million sentences instead?
#
# R2. GloVe (which you used in word2vec.py) is NOT the same algorithm as
#     Word2Vec. What is the core difference in how they are trained?
#     (Hint: global matrix factorization vs. local context window)
#
# R3. Both Word2Vec and GloVe produce WORD embeddings — one vector per word.
#     What is the problem with that for a sentence like:
#     "I went to the river bank" vs "I deposited money at the bank"?
#     What type of model solves this? (This is your preview of the next lesson.)
# ---------------------------------------------------------------------------

# R1: TODO
# R2: TODO
# R3: TODO
