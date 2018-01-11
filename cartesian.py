import numpy as np

def cartesian(*arrays):
    mesh = np.meshgrid(*arrays)  # standard numpy meshgrid
    dim = len(mesh)  # number of dimensions
    elements = mesh[0].size  # number of elements, any index will do
    flat = np.concatenate(mesh).ravel()  # flatten the whole meshgrid
    reshape = np.reshape(flat, (dim, elements)).T  # reshape and transpose
    return reshape


k1=np.arange(-2.0, 3,1)
k2=np.arange(-2.0, 3,1)
k3=np.arange(-2.0, 3,1)
k4=np.arange(-2.0, 3,1)
k5=np.arange(-2.0, 3,1)
k6=np.arange(-2.0, 3,1)
k7=np.arange(-2.0, 3,1)
k8=np.arange(-2.0, 3,1)
k9=np.arange(-2.0, 3,1)
a = cartesian(k1,k2,k3,k4,k5,k6,k7,k8,k9)
print(a)
print len(a)