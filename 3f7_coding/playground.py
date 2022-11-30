p = {'a': 0.06459594975000238, 'b': 0.06416702675532909, 'c': 0.06613733728513503, 'd': 0.06447508131543389, 'e': 0.09941757570704181, 'f': 0.08776497294617328, 'g': 0.049928909356391965, 'h': 0.045471892928494934,
          'i': 0.03860085507614455, 'j': 0.08399539581856305, 'k': 0.08213393244462111, 'l': 0.06883307765368174, 'm': 0.04542700167100284, 'n': 0.02483897643347246, 'o': 0.029761092368437915, 'p': 0.08445092249007394}


from math import log2, ceil

def shannon_fano(p):

    # Begin by sorting the probabilities in decreasing order, as required
    # in Shannon's paper.
    p = dict(sorted([(a,p[a]) for a in p if p[a]>0.0], key = lambda el: el[1], reverse = True))

    # Compute the cumulative probability distribution
    # this can be done easily with numpy.cumsum but we will do it by hand. Note
    # that this is not a time-critical operation so efficiency is not an issue.
    
    # step 1: initialise f to be a list with one element 0 (this is because Shannon
    # requires the cumulative probability to be the sum up to AND EXCLUDING the current
    # symbol, so the first element of f should be zero.
    
    f = [0] # (whenever you see "..." you are expected to complete a missing command

    # step 2: compute the runninng sum
    for a in p: # for every probability in p
        # you now want to append to f the sum of its last entry (which you can access as [-1])
        # and the probability p[a] of the current symbol

        f.append(p[a]+f[-1])

    # the resulting cumulative has one too many element at the end, the sum of all probabilities
    # that should equal to one. You can use the "pop" command to delete the last element in a list.

    f.pop()

    # We now convert the list you computed into a dictionary
    f = dict([(a,mf) for a,mf in zip(p,f)])
    print(f)
    # assign the codewords
    code = {} # initialise as an empty dictionary
    for a in p: # for each probability

        # Compute the codeword length according to the Shannon-Fano formula
        # you want to use the functions "ceil()" and "log2()" we imported
        # from the math library
        length = ceil(-log2(p[a]))
        # (assign variable name "length")


        codeword = [] # initialise current codeword
        myf = f[a]
        # for each position in length, we will multiply myf by 2 and take the
        # integral part as our binary digit
        for pos in range(length):
            # multiply myf by 2 (shifting it "left" in binary)
            myf *= 2

            # if the resulting myf is larger than 1, append a 1 to the codeword,
            # whereas if it is smaller than 1 you should append a 0
            # If it is larger than 1, you sould also substratct 1 from myf.
            if myf >= 1:
                codeword.append(1)
                myf -= 1
            else:
                codeword.append(0)

        code[a] = codeword # assign the codeword
        
    return code # return the code table

print(shannon_fano(p))