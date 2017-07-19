from sklearn.datasets.samples_generator import make_blobs

n_f = 3000000
n_s = 10
X, y = make_blobs(n_samples=n_s, centers=2, n_features=n_f)
f = open('test.out', 'w')
for i in range(n_s):
    print i
    f.write(str(y[i]))
    f.write(",")
    for w in range(n_f):
        f.write(str(X[i][w]))
        f.write(',')
    f.write("\n")
