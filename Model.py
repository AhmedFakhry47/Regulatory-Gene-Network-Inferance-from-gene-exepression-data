from sklearn.metrics import roc_curve,roc_auc_score
import tensorflow as tf
import numpy as np
import json

class Shallow_M (tf.keras.Model):
  def __init__(self,n_classes=1,act='sig'):
    super(Shallow_M,self).__init__()
    
    self.DenseP   = tf.keras.layers.Dense(256,activation=tf.nn.relu)
    self.BatchN_P = tf.keras.layers.BatchNormalization(momentum=0.9)
    self.DropO_P  = tf.keras.layers.Dropout(rate=0.5)    
    
    self.DenseA   = tf.keras.layers.Dense(256,activation=tf.nn.relu)
    self.BatchN_A = tf.keras.layers.BatchNormalization(momentum=0.9)
    self.DropO_A  = tf.keras.layers.Dropout(rate=0.5)    
    
    self.DenseB   = tf.keras.layers.Dense(256,activation=tf.nn.relu)
    self.BatchN_B = tf.keras.layers.BatchNormalization(momentum=0.9)
    self.DropO_B  = tf.keras.layers.Dropout(rate=0.5)    
    
    if (act == 'sig'):
      self.Predict  = tf.keras.layers.Dense(n_classes,activation=tf.nn.sigmoid)
    else:
      self.Predict  = tf.keras.layers.Dense(n_classes,activation=tf.nn.softmax)

  def call(self,inputs,training=False):
    x = tf.math.reduce_mean(inputs,axis=1)
    
    p = self.DenseP(inputs[:,0,:])
    p = self.BatchN_P(p)
    p = self.DropO_P(p)

    x = self.DenseA(x)
    x = self.BatchN_A(x,)
    x = self.DropO_A(x,training=training)
    
    x = self.DenseB(x)
    x = self.BatchN_B(x,)
    x = self.DropO_B(x,training=training)

    out = tf.keras.layers.concatenate([x,p])

    return self.Predict(out)
  
  