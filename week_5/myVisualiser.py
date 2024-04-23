import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
def cluster_and_visualise(datafilename, K, featureNames):
    data = np.genfromtxt(datafilename)
    clusterModel = KMeans(n_clusters=2)
    clusterModel.fit(data)
    

