# 6.02 PS: Syndrome decoding of a linear block code
from numpy import *
import numpy
import PS2_tests

# Replace each entry of a matrix A with its modulo 2 value 
# and return that matrix.  All your base are belong to 2. :-)
def mod2(A):
    for i in range(2):
        A[A%2==i] = i
    return A

# True iff two matrices are identical element-by-element.
def equal(a, b):
    if (a == b).all():
        return True
    return False

# Assume that the code has Hamming distance 3, 
# i.e., correct all patterns of 1-bit errors in the n-bit codeword.
# n and k are positive integers; n > k and G is a numpy matrix for the code.
# Return a numpy array of length k, each entry either 0 or 1, 
# corresponding to the k decoded *message* bits.  We return codeword[:k] 
# in the template; you can preserve that, or change it as you wish.
def syndrome_decode(codeword, n, k, G):
    ## YOUR CODE HERE
    # print(codeword)
    A = G[:, k:n+1]
    # print("A", A)
    # print("G", G)
    I = numpy.identity(n-k)
    Atransposed = A.getT()
    H = numpy.concatenate((Atransposed, I), axis=1)
    # print("H", H)
    CodewordTransposed = codeword.transpose()
    # print("CodewordTransposed", CodewordTransposed)
    result = numpy.dot(H, CodewordTransposed)
    mod2Result = mod2(result)

    # print(mod2Result)

    if equal([0*k], mod2Result):
        return codeword[:k]
    ##find the correct syndrome if there is one that exists
    for i in range(n):
        Hcolumn = H[:, i]
        if equal(Hcolumn.transpose(), mod2Result):
            # print(mod2Result)
            # print("we found an error at bit", i)
            copy = codeword
            copy[i] ^= 1
            return copy[:k]
    return codeword[:k]

if __name__ == '__main__':
    # (7,4,3) Hamming code
    G1 = matrix('1 0 0 0 1 1 0; 0 1 0 0 1 0 1; 0 0 1 0 0 1 1; 0 0 0 1 1 1 1', 
                dtype=int)
    PS2_tests.test_linear_sec(syndrome_decode, 7, 4, G1)

    # (8,4,3) rectangular parity code
    G2 = matrix('1 0 0 0 1 0 1 0; 0 1 0 0 1 0 0 1; 0 0 1 0 0 1 1 0; 0 0 0 1 0 1 0 1', dtype=int)
    PS2_tests.test_linear_sec(syndrome_decode, 8, 4, G2)

     # (6,3,3) pairwise parity code
    G3 = matrix('1 0 0 1 1 0; 0 1 0 0 1 1; 0 0 1 1 0 1', dtype=int)
    PS2_tests.test_linear_sec(syndrome_decode, 6, 3, G3)
    
    # (15,11,3) Hamming code
    G4 = matrix('1 0 0 0 0 0 0 0 0 0 0 0 1 1 1; 0 1 0 0 0 0 0 0 0 0 0 1 0 1 1; 0 0 1 0 0 0 0 0 0 0 0 1 1 0 1; 0 0 0 1 0 0 0 0 0 0 0 1 1 1 0; 0 0 0 0 1 0 0 0 0 0 0 1 1 1 1; 0 0 0 0 0 1 0 0 0 0 0 1 1 0 0; 0 0 0 0 0 0 1 0 0 0 0 1 0 1 0; 0 0 0 0 0 0 0 1 0 0 0 1 0 0 1; 0 0 0 0 0 0 0 0 1 0 0 0 1 1 0; 0 0 0 0 0 0 0 0 0 1 0 0 1 0 1; 0 0 0 0 0 0 0 0 0 0 1 0 0 1 1')
    PS2_tests.test_linear_sec(syndrome_decode, 15, 11, G4)
