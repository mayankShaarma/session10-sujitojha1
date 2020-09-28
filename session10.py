# Session 8 Assignment - Closure
# Author: Sujit Kumar Ojha
# email : sujit.ojha@gmail.com

def gen_fx_to_check_doc_string():
    """ Closure function to generate function to check doc string length > 50
    Returns:
        inner: function
    """
    doc_str_threshold = 50
    def doc_length_check(fn):
        fn_len = len(fn.__doc__.replace("\n",""))
        print('Docstring: {0}\nCharacter Count = {1}'.format(fn.__doc__,fn_len))
        return fn_len > doc_str_threshold
    return doc_length_check

# Creating a function to check the doc string length is greater than 50
check_doc_string = gen_fx_to_check_doc_string()

def gen_fx_next_fib_num():
    """ Closure function to generate next fibonacci number
    Returns:
        fibonacci: function
    """
    fib1 = 0
    fib2 = 0
    def fibonacci():
        nonlocal fib1, fib2
        if fib1 ==0 and fib2 ==0:
            fib2 = 1
        else:
            fib2, fib1 = fib1+ fib2, fib2
        return fib1
    return fibonacci

# Creating a function to generate the next fibonacci number
fibonacci = gen_fx_next_fib_num()

def add(a, b):
    """ Simple number addition function
    Boundary c
    """
    return a + b
def mul(a, b):
    """ Simple number multiplication function
    Bound
    """
    return a*b
def div(a, b):
    """ Simple number division function
    """
    return a/b

cnt={}
def counter(fn):
    """ Closure function to create a counter function 
    Counter will be saved as dictionary with key as function name
    Args:
        fn: function call to be counted
        cnt: is global counter
    Return:
        inner: function
    """
    key = ""
    def inner(*args, **kwargs):
        global cnt
        nonlocal key
        key = fn.__name__
        if key not in cnt:            
            cnt[key] = 0
        cnt[key] += 1
        print('{0} has been called {1} times'.format(fn.__name__, cnt[key]))
        return fn(*args, **kwargs)
    return inner


def user_counter(fn,cnt):
    """ Closure function to create a counter function 
    Counter will be saved as dictionary with key as function name
    Args:
        fn: function call to be counted
        cnt: user defined counter for each user different
    Return:
        inner: function
    """
    key = ""
    def inner(*args, **kwargs):
        nonlocal key
        key = fn.__name__
        if key not in cnt:            
            cnt[key] = 0
        cnt[key] += 1
        print('{0} has been called {1} times'.format(fn.__name__, cnt[key]))
        return fn(*args, **kwargs)
    return inner