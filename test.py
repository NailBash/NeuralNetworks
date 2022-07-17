import numpy as np, tensorflow as tf

tf.compat.v1.disable_eager_execution()

n_samples,batch_size,num_steps=1000,100,20000

X_data=np.random.uniform(1,10,(n_samples,1))
Y_data=2*X_data+1+np.random.normal(0, 2, (n_samples, 1))



print("I'm here")