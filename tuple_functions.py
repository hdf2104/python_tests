'''
Several useful functions(or methods) for doing things with tuples
'''

def TVCKWA (a_tup=(2,3,4,5), an_int=6) :
    '''this returns the input with an_int as the first term'''
    print a_tup, an_int
    print a_tup[1:]
    print a_tup *2
    print (an_int,) + a_tup[1:]
    #need oto create a new tuple that looks like above that is sliced
    new_tup = (an_int,) + a_tup[1:]
    #new_tup = new_tup + a_tup[1:] is the same as new_tup += a_tup[1:]
    return new_tup

def print_tuple( tup = (1,2,3) ) :
    '''prints a tuple, no return value '''
    return tup
