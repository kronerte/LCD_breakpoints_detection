import numpy as np 
import CoordinateDescent as CD


#########################################################################################
#
# Date : 10/06/2020
# Author : Etienne Kronert
# Team : Modal - INRIA
#
#########################################################################################

class LCDBD():
    def __init__(self, Lambda = None, C = 3, eps_thres = 1e-3):
        self.Lambda = Lambda
        self.C = C
        self.eps_thres = eps_thres

    def fit(self, Y):
        if self.Lambda is None:
            n = Y.shape[0]
            self.Lambda = self.C*np.sqrt(np.log(n)/n)
        self.beta = CD.LASSO_CD(Y, n*self.Lambda, self.eps_thres)

    def predict(self):
        return self.beta

    def fit_predict(self, Y):
        self.fit(Y)
        return self.predict()