# template file for 6.02 PS1, Python Task 4 (LZW Compression/Decompression)
import sys
from optparse import OptionParser
import struct
import array


def initializeArray():
    table = []
    for i in range(256):
        # table[i] = chr(i)
        # table[chr(i)] = i
        table.append(chr(i))

    return table
def compress(filename):
    """
    Compresses a file using the LZW algorithm and saves output in another file.
    Arguments: 
        filename: filename of file to compress.
    Returns:
        None.
    """
    try:
        outputName = filename + '.zl'
        table = initializeArray()
        with open(filename, 'rb') as file:
            #read one byte at a time when compressing a file
            with open(outputName, 'wb') as outFile:
                # string = array.array("B", file.read())
                # symbol = array.array("B", file.read())
                # while symbol:
                # while symbol != '10':
                #     if string + symbol in table:
                #         string = string + symbol
                #         print(string)
                #     else:
                #         # outFile.write(table.index(string))
                #         table.append(string + symbol)
                #         string = symbol
                #     symbol = array.array("B", file.read())
                # outFile.write(table.index(string))

                compressed = array.array("B", file.read())
                string = chr(compressed[0])
                for symbol in compressed[1:]:
                    symbol = chr(symbol)
                    print(string + symbol)
                    if string + symbol in table:
                        string = string + symbol
                        print(string)
                    else:
                        outFile.write(table.index(string).to_bytes(2, 'little'))
                        table.append(string + symbol)
                        string = symbol
                outFile.write(table.index(string).to_bytes(2, 'little'))


    except FileNotFoundError:
        print ("This File %s does not exist", filename)

def uncompress(filename):
    """
    Decompresses a file using the LZW algorithm and saves output in another file.
    Arguments: 
        filename: filename of file to decompress.
    Returns:
        None.
    """
    try:
        outputName = filename + ".u"
        table = initializeArray()

        with open(filename, 'rb') as file:
            #read one byte at a time when compressing a file
            with open(outputName, 'w') as outFile:
                compressed = array.array("H", file.read())
                string = table[compressed[0]]
                outFile.write(string)
                # print(compressed)
                entry = ""
                for code in compressed[1:]:
                    if code >= len(table):
                        entry = string + string[0]
                    else:
                        entry = table[code]
                    outFile.write(entry)
                    table.append(string+entry[0])
                    string = entry
    except FileNotFoundError:
        print("This file %s does not exist", filename)

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-f", "--filename", type="string", dest="fname", 
                      default="test", help="file to compress or uncompress")
    parser.add_option("-c", "--compress", action="store_true", dest="uncomp", 
                      default=True, help="compress file")
    parser.add_option("-u", "--uncompress", action="store_true", dest="uncomp", 
                      default=False, help="uncompress file")

    (opt, args) = parser.parse_args()
    
    if opt.uncomp == True:
        uncompress(opt.fname)
    else:
        compress(opt.fname)
