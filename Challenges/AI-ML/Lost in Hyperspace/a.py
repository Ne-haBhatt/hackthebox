import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

data = np.load('token_embeddings.npz')
tokens = data['tokens']
embeddings = data['embeddings']

pca = PCA(n_components=2)
re_embeddings = pca.fit_transform(embeddings)

plt.figure(figsize=(20, 12))
plt.scatter(re_embeddings[:, 0], re_embeddings[:, 1], alpha=0.6, s=100, edgecolor='k')
for i, token in enumerate(tokens):
    plt.text(re_embeddings[i, 0] + 0.02, re_embeddings[i, 1], str(token), fontsize=12, fontweight='bold')

plt.title('token embeddings PCA:')
plt.xlabel('1 principal component')
plt.ylabel('2 principal component')
plt.grid(False)
plt.show()