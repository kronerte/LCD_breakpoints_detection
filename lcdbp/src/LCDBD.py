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
    """ Class that perform breakpoints detection using the Lasso framework and solved using Coordinate Descent.
    The API of this class is based on Scikit-learn estimators.
    
    :parameters:
    - Lambda : Regularisation parameter of the LASSO
    - C :  Parameter use to compute Lambda if not provided
    - eps_thres :  control the convergence of the Coordinate Descent
    - beta_hat : solution of the LASSO
    
    :methods:
    - __init__ : Instanciate the class
    - fit : solve the LASSO problem
    - predict : return the sparse beta, the jump vector estimator 
    - fit_predict : performs fit and predict sequentially
    """
    def __init__(self, Lambda = None, C = 3, eps_thres = 1e-3):
        """
        Instanciate the class
        :parameters:
        - Lambda : Regularisation parameter of the LASSO
        - C :  Parameter use to compute Lambda if not provided
        - eps_thres :  control the convergence of the Coordinate Descent
        """
        self.Lambda = Lambda
        self.C = C
        self.eps_thres = eps_thres

    def fit(self, Y):
        """
        Solve the LASSO problem
        :parameters:
        - Y : vector of observations
        """
        if self.Lambda is None:
            n = Y.shape[0]
            self.Lambda = self.C*np.sqrt(np.log(n)/n)
        self.beta_hat = CD.LASSO_CD(Y, n*self.Lambda, self.eps_thres)

    def predict(self):
        """return the sparse beta, the jump vector estimator
        
        :return:
        - beta_hat: the jump vector estimator"""
        return self.beta_hat

    def fit_predict(self, Y):
        """
        performs fit and predict sequentially
        :parameters:
        - Y : vector of observations
        :return:
        - beta_hat: the jump vector estimator
        """
        self.fit(Y)
        return self.predict()