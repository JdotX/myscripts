# Testing Distributed Tensorflow

***

Normally in academic papers people use different applications to test distributed machine learning systems performance.

- Matrix Factorization (MaF): in mf_dis.py. Note the data (matrix input) is not yet splitted.
- Image Classification (ImC): in complex_MNIST.py. This implementation is nearly minimal with 2 convolutional layers and 1 fully connections layers. In real test we can easily add layers.
- Topic Detection (ToD): TODO.

***

# Todos:

- Implement a ToD case
- MaF data split
