# Programa de classifição por mínimos quadrados




#import numpy as np
#import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier



X = [[0., 0.], [1., 1.]]
y = [0, 1]





clf = SGDClassifier(loss="hinge", penalty="l2", max_iter=5)
clf.fit(X, y)   
SGDClassifier(alpha=0.0001, average=False, class_weight=None,
           early_stopping=False, epsilon=0.1, eta0=0.0, fit_intercept=True,
           l1_ratio=0.15, learning_rate='optimal', loss='hinge', max_iter=5,
           n_iter_no_change=5, n_jobs=None, penalty='l2', power_t=0.5,
           random_state=None, shuffle=True, tol=0.001,
           validation_fraction=0.1, verbose=0, warm_start=False)


clf.predict([[2., 2.]])

clf.coef_
