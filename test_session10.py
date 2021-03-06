import pytest
import random
import string
import session10
import os
import inspect
import re
import time

CONTENT_CHECK_FOR = [
    'Faker',
    'profile',
    'namedtuple',
    'largest_blood_type',
    'mean_current_location',
    'oldest_person_age',
    'average_age',
    'faker_company_stock_data',
    'stock_market_status',
    'company'
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
    functions = [session10.largest_blood_type, 
                 session10.mean_current_location,
                 session10.oldest_person_age,
                 session10.average_age,
                 session10.faker_company_stock_data,
                 session10.stock_market_status]

    for function in functions:
        assert not function.__annotations__ is None, "You have dont have annotations defined for {}".format(function.__name__)

def test_named_tuple_doc_string():
    doc_string = session10.profile.__doc__
    ssn_doc_string = session10.profile.ssn.__doc__

    assert 'Faker library' in doc_string, "Check profile named tuple doctring"
    assert "Social Security Number" in ssn_doc_string, "Check profile named tuple doctring"

def test_named_tuple_performance_vs_dict():
    ntple_time, dict_time = session10.largest_blood_type(session10.fake_profiles_tupple, session10.profiles_dict)
    assert ntple_time<dict_time, "Check the largest blood type function performance for named tuple"

    ntple_time,dict_time = session10.mean_current_location(session10.fake_profiles_tupple,session10.profiles_dict)
    assert ntple_time<dict_time, "Check the mean_current_location function performance for named tuple"

    ntple_time,dict_time = session10.oldest_person_age(session10.fake_profiles_tupple,session10.profiles_dict)
    assert ntple_time<dict_time, "Check the oldest_person_age function performance for named tuple"

    ntple_time,dict_time = session10.average_age(session10.fake_profiles_tupple,session10.profiles_dict)
    assert ntple_time<dict_time, "Check the average_age function performance for named tuple"

def test_stock_market_status_conditions():
    stock_market_today_start, stock_market_today_high, stock_market_today_close = session10.stock_market_status(session10.company_stock_market_tupple)

    assert stock_market_today_high>=stock_market_today_start, "Check the stock market data as high value should be higher than or equal open value always"

    assert stock_market_today_high>=stock_market_today_close, "Check the stock market data as high value should be higher than or equal close value always"