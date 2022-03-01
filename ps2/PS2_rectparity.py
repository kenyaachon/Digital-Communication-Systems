# template for 6.02 rectangular parity decoding using error triangulation
import PS2_tests
import numpy


def parity_rowCalc(codeword, nrows, ncols):
    row_errors = []
    for i in xrange(1, nrows+1):
        total = 0
        for j in xrange(1, ncols+1):
            total += codeword[i*j - 1]
        total += codeword[nrows*ncols + i - 1]
        if total % 2 != 0:
            row_errors.append(i)

    return row_errors

def parity_columnCalc(codeword, nrows, ncols):
    column_errors = []
    for i in range(1, ncols+1):
        total = 0
        colpos = i
        for j in range(1, nrows+1):
            total += codeword[colpos - 1]
            colpos += ncols
            # print (colpos - 1)
            # print("data bit", codeword[colpos - 1])
        total += codeword[nrows*ncols + nrows + i - 1]
        # print (nrows*ncols + nrows + i - 1)
        # print("column parity bit", codeword[nrows*ncols + nrows + i - 1])
        if total %2 != 0:
            column_errors.append(i)

    return column_errors

def rect_parity(codeword,nrows,ncols): 
    ## YOUR CODE HERE
    ## return the corrected data
    columns = parity_columnCalc(codeword, nrows, ncols)
    rows = parity_rowCalc(codeword, nrows, ncols)

    print "result from columns", columns
    print "result from rows", rows

    if len(columns) == 0 and len(rows) == 0:
        return codeword[:ncols*nrows]
    elif len(columns) == 1 and len(rows) == 1:
        print "flipping the data bit"
        copy = codeword 
        copy[columns[0]*rows[0] - 1] ^= 1
        return copy[:ncols*nrows]
    elif (len(columns) == 1 and len(rows) == 0) or (len(columns) == 0 and len(rows) == 1):
        return codeword[:ncols*nrows]
    else:
        return codeword[:ncols*nrows]
if __name__ == '__main__':
    # PS2_tests.test_correct_errors(rect_parity)
    # codeword = [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0]
    # rect_parity(codeword, 2, 4)

    # codeword = [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0]
    # rect_parity(codeword, 2, 4)

    codeword = [0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1]
    print(rect_parity(codeword, 2, 4))
