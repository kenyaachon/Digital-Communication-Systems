import sys
from optparse import OptionParser
import struct
import array

###Key Note: this works best with Python 2.7, otherwise Python 3.9 causes
###an encoding error
####


def initializeArray():
    table = []
    for i in range(256):
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

                compressed = array.array("B", file.read())
                string = chr(compressed[0])
                for code in compressed[1:]:
                    symbol = chr(code)
                    if string + symbol in table:
                        string = string + symbol
                    else:
                        outFile.write(struct.pack("<H", table.index(string)))
                        table.append(string + symbol)
                        string = symbol
                outFile.write(struct.pack("<H", table.index(string)))


    # except FileNotFoundError:
    except IOError:
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
                entry = ""
                for code in compressed[1:]:
                    if code >= len(table):
                        entry = string + string[0]
                    else:
                        entry = table[code]
                    outFile.write(entry)
                    table.append(string+entry[0])
                    string = entry
                print(len(table))
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
