import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.manifold import MDS 

data = np.load( 'distance_matrix.npy' ) 
mds = MDS(n_components= 2 , dissimilarity= 'precomputed' , random_state= 42 ) 
X = mds. fit_transform(data) 
plt.scatter(X[:, 0 ], X[:, 1 ]) 
plt.savefig( '.png' ) 
plt.show()
