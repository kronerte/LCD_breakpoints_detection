import numpy as np 

#########################################################################################
#
# Date : 10/06/2020
# Author : Etienne Kronert
# Team : Modal - INRIA
#
########################################################################################


def prodXTv(v):
    """
    Fast computation function for the product between a vector v  
    and the transpose of the triangular matrix X with only one below the diagonal.
    
    :parameters:
    - v : (array-like) the vector v
    
    :return:
    - res : the result of the matrix-vector product"""
    return np.cumsum(v[::-1])[::-1]


def prodXTXv(v):
    """
    Fast computation function for the product between a vector v, the matrix X and the transpose of the matrix X, 
    where X is the triangular matrix with only one below the diagonal.
    
    :parameters:
    - v : (array-like) the vector v
    
    :return:
    - res : the result of the matrix-vector product"""
    return np.cumsum(np.cumsum(v)[::-1])[::-1]


def prodXiTXv(v,i):
    """
    Fast computation function for the product between a vector v, the matrix X and the transpose of the i-th row of the matrix X, 
    where X is the triangular matrix with only one below the diagonal.
    
    :parameters:
    - v : (array-like) the vector v
    
    :return:
    - res : the result of the matrix-vector product"""
    return np.cumsum(v)[i:].sum()



def append_sort(L, a, n):
    """ Add an element in a sorted List and keep the constrain of sorted and no duplicate.

    Use Insertion sort.
    
    :parameters:
    - L : the sorted List
    - a : the element we want to place in the list
    - n : the size of the list
    
    :return:
    - L : the sorted list with the new element append"""
    if a in L:
        None
    elif n == 0 or L[-1]<a:
        L.append(a)
    else:
        for (ind, el) in enumerate(L):
            if el > a:
                L = L[:ind] + [a] + L[ind:]
                break
    return L