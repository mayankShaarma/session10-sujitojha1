import pytest
import random
import string
import session10
import os
import inspect
import re
import time

CONTENT_CHECK_FOR = [
    'gen_fx_to_check_doc_string',
    'check_doc_string',
    'gen_fx_next_fib_num',
    'fibonacci',
    'add',
    'mul',
    'div',
    'cnt',
    'counter',
    'user_counter'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session10)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        #print(len(space) % 4,space)
        #assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session10, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_all_functions_with_docstrings():
    functions = inspect.getmembers(session10, inspect.isfunction)

    for function in functions:

        assert not function.__doc__ is None, f"You have dont have docstring defined for {function}"

def test_all_functions_with_annotations():
    functions = [session10.gen_fx_to_check_doc_string, 
                 session10.gen_fx_next_fib_num,
                 session10.add,
                 session10.counter,
                 session10.user_counter]

    for function in functions:
        assert not function.__annotations__ is None, "You have dont have annotations defined for {}".format(function.__name__)

def test_all_methods_defined():
    ALLMETHODSDEFINED = True
    f = open("session10.py", "r")
    content = f.read()
    f.close()
    for c in CONTENT_CHECK_FOR:
        if c not in content:
            ALLMETHODSDEFINED = False
            #print(c)
            pass
    assert ALLMETHODSDEFINED == True, "You have not covered all methods in session10.py file"

# def test_isfibonacci_valueerror():
#     with pytest.raises(ValueError):
#         assert session10.is_fibonnaci(-1)
#     with pytest.raises(ValueError):
#         assert session10.is_fibonnaci(12000)
#     with pytest.raises(ValueError):
#         assert session10.is_fibonnaci("1")
#     with pytest.raises(ValueError):
#         assert session10.is_fibonnaci(7.1)

def test_gen_fx_to_check_doc_string_isclosure():
    assert bool(session10.check_doc_string.__closure__) == True, "Check the gen_fx_check_string_function, it is not defined as closure"

def test_gen_fx_to_check_doc_string_freevars():
    assert session10.check_doc_string.__code__.co_freevars[0] == 'doc_str_threshold', "Check the gen_fx_check_string_function, it is not defined as closure"

def test_check_doc_string_function():
    assert bool(session10.check_doc_string(session10.gen_fx_to_check_doc_string)) == True, "Check the check_doc_string function !!!"
    assert bool(session10.check_doc_string(session10.gen_fx_next_fib_num)) == True, "Check the check_doc_string function !!!"
    assert bool(session10.check_doc_string(session10.add)) == False, "Check the check_doc_string function !!!"
    assert bool(session10.check_doc_string(session10.mul)) == True, "Check the check_doc_string function !!!"
    assert bool(session10.check_doc_string(session10.div)) == False, "Check the check_doc_string function !!!"
    assert bool(session10.check_doc_string(session10.counter)) == True, "Check the check_doc_string function !!!"
    assert bool(session10.check_doc_string(session10.user_counter)) == True, "Check the check_doc_string function !!!"

def test_gen_fx_next_fib_num_isclosure():
    assert bool(session10.fibonacci.__closure__) == True, "Check the gen_fx_next_fib_num function, it is not defined as closure"

def test_gen_fx_next_fib_num_freevars():
    assert len(session10.fibonacci.__code__.co_freevars) == 2, "Check the gen_fx_next_fib_num function, it is not defined as closure"

def test_fibonacci_function():
    fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    gen_list = [session10.fibonacci() for _ in range(10)]
    assert fib_list==gen_list, "Check fibonacci function for generating first 10 numbers"


def test_counter_isclosure():
    count_add = session10.counter(session10.add)
    assert bool(count_add.__closure__) == True, "Check the counter function, it is not defined as closure"

def test_counter_freevars():
    count_add = session10.counter(session10.add)
    assert len(count_add.__code__.co_freevars) == 2, "Check the counter function, free variable not set propeorly"

def test_counter_function():
    count_add = session10.counter(session10.add)
    count_mul = session10.counter(session10.mul)
    count_div = session10.counter(session10.div)
    for i in range(5):
        count_add(1,2)
    for i in range(10):
        count_mul(1,2)
    for i in range(2):
        count_div(1,2)
    assert session10.cnt['add'] == 5, "Check the counter function, counter specifically !!!"
    assert session10.cnt['mul'] == 10, "Check the counter function, counter specifically !!!"
    assert session10.cnt['div'] == 2, "Check the counter function, counter specifically !!!"

def test_user_counter_isclosure():
    user1={}
    count_add = session10.user_counter(session10.add,user1)
    assert bool(count_add.__closure__) == True, "Check the user counter function, it is not defined as closure"

def test_gen_user_counter_freevars():
    user1={}
    count_add = session10.user_counter(session10.add,user1)
    assert len(count_add.__code__.co_freevars) == 3, "Check the user counter function, free variable not set propeorly"

def test_user_counter_function():
    user1,user2,user3={},{},{}
    count_add1 = session10.user_counter(session10.add,user1)
    count_mul1 = session10.user_counter(session10.mul,user1)
    count_div1 = session10.user_counter(session10.div,user1)
    for i in range(5):
        count_add1(1,2)
    for i in range(10):
        count_mul1(1,2)
    for i in range(2):
        count_div1(1,2)
    count_add2 = session10.user_counter(session10.add,user2)
    count_mul2 = session10.user_counter(session10.mul,user2)
    count_div2 = session10.user_counter(session10.div,user2)
    for i in range(3):
        count_add2(1,2)
    for i in range(15):
        count_mul2(1,2)
    for i in range(4):
        count_div2(1,2)
    count_add3 = session10.user_counter(session10.add,user3)
    count_mul3 = session10.user_counter(session10.mul,user3)
    count_div3 = session10.user_counter(session10.div,user3)
    for i in range(7):
        count_add3(1,2)
    for i in range(8):
        count_mul3(1,2)
    for i in range(9):
        count_div3(1,2)
    assert user1['add'] == 5, "Check the counter function, counter specifically !!!"
    assert user1['mul'] == 10, "Check the counter function, counter specifically !!!"
    assert user1['div'] == 2, "Check the counter function, counter specifically !!!"

    assert user2['add'] == 3, "Check the counter function, counter specifically !!!"
    assert user2['mul'] == 15, "Check the counter function, counter specifically !!!"
    assert user2['div'] == 4, "Check the counter function, counter specifically !!!"

    assert user3['add'] == 7, "Check the counter function, counter specifically !!!"
    assert user3['mul'] == 8, "Check the counter function, counter specifically !!!"
    assert user3['div'] == 9, "Check the counter function, counter specifically !!!"
