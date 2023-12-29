import os
os.environ["TF_ENABLE_ONEDNN_OPTS"]="0"
import tensorflow as tf
input_tensor = tf.constant([[1,2,3],[4,5,6]])
transposed_tensor = tf.transpose(input_tensor)
print(transposed_tensor)

import numpy as np
input_array = np.array([[1,2,3],[4,5,6]])
tansposed_array = np.transpose(input_array)
print(input_array)
# AX=B => inv(A)AX=inv(A)B   => IX=inv(A)B => X=inv(A)B
import numpy as np
input_array = np.array([[1,1,1],[2,-1,1],[4,1,-1]])
array=np.array([[9],[5],[7]])

#tf.linalg.inv
output_array = np.linalg.inv(input_array)
print(output_array)
out=output_array@array
print(out)
