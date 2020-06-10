import numpy as np 
import utils

#########################################################################################
#
# Date : 10/06/2020
# Author : Etienne Kronert
# Team : Modal - INRIA
#
#########################################################################################



def LASSO_CD(Y, Lambda, eps_thres = 1e-3):
    """ Resolve the LASSO problem for the specific matrix X : triangalar with only one below the diagonal.
    The Lasso is solved by alternating coordinate descent and active set update.

    :parameters:
    - Y : vector of observations
    - Lambda : regularisation parameter of the Lasso
    - eps-thres : Hyperparameter that control the convergence of the algorithm

    :return:
    - beta : solution of the LASSO"""

    # INITIALISATION
    n = Y.shape[0]
    A = []
    beta = np.zeros(n)
    c = utils.prodXTv(Y)
    sizeA = 0

    while True:
        # COORDINATE DESCENT
        if sizeA>0:
            beta = CoordinateDescent(beta, Lambda, A, c = c, Y = None,
                                     n = n, eps_thres =eps_thres)
                
        # ACTIVE SET UPDATING

        # 1) remove the coordinate that leave the active set
        A = [i for i in A if beta[i] != 0] 
        
        # 2) Add a new coordinate in the active set
        sizeA = len(A)
        S = c - utils.prodXTXv(beta) 
        S_norm = np.abs(S)
        S_norm[A] = 0
        u_hat = np.argmax(S_norm)
        M = S_norm[u_hat]**2
        # Check if KKT is satified
        if M>Lambda**2 and not u_hat in A:
            A = utils.append_sort(A, u_hat, sizeA)
            sizeA += 1
        
        else: 
            return beta







def CoordinateDescent(beta, Lambda, A, c = None, Y = None, n = None, eps_thres = 1e-3):
    """ Use the Coordinate Descent Algorithm in order to optimize the LASSO on the active set A.
    
    :parameters:
    - beta : the current weights vector we want to optimize
    - Lambda : regularisation parameter of the Lasso
    - A : Active set (list of coordinate that are not equal to zero)
    - c : vector of correlation (if not provided, it would be automatically computed)
    - Y : vector of observation (needed only to compute c, if c is not provided)
    - n : number of observations (if not provided, it would be calculated)
    - eps-thres : Hyperparameter that control the convergence of the algorithm
    
    :return:
    - beta : beta vector after optimization on the active set
    - """
    if c is not None:
        c = utils.prodXTv(Y)
    if n is not None:
        n = beta.shape[0]
    epsilon = 1
    while epsilon > 1e-3:
        beta0 = np.copy(beta)
        for i in A:
            beta_i = np.copy(beta)
            beta_i[i] = 0
            rho = c[i] - utils.prodXiTXv(beta_i,i)   
            zi = n-i  
            if rho < -Lambda/2 :
            
                beta[i] = (rho + Lambda/2)/zi   
            elif rho < Lambda/2:
                beta[i] = 0   
            else :
                beta[i] = (rho - Lambda/2)/zi

        epsilon = np.linalg.norm(beta0-beta)
    return beta


