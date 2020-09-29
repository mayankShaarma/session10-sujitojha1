# session10-sujitojha1, Tuples and Named Tuples
TSAI EPAi Session 8 Assignment

## 1. Objective: Scopes and Closures

- Use Faker library to get 10000 random profiles. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age and average age (add proper doc-strings).
- Do the same thing above using a dictionary. Prove that namedtuple is faster.
- Create a fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. - Calculate and show what value stock market started at, what was the highest value during the day and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple.
- Add the notebook as well to your github where logs can be visible. 

- No readme or no docstring for each function, or no test cases, 0. Write test cases to check boundary conditions that might cause your code to fail. 

## 3. Documentation for functions

CONTENT_CHECK_FOR = [
    'Faker',
    'profile'
    'namedtuple',
    '__doc__',
    'largest_blood_type',
    'mean_current_location',
    'oldest_person_age',
    'average_age',
    'faker_company_stock_data',
    'stock_market_status',
    'company'
]

**gen_fx_to_check_doc_string** :  
    - Its a closure function which generate function to test doc string length > 50  
    - doc_str_threshold is free variable  
```python
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
```
**check_doc_string**  
    - it function created using above closure function  

**gen_fx_next_fib_num**  
    - Its a closure function that generates function to get next fibonacci number  
    - Two free variables fib1 and fib2 to manage first two values of fibonacci  
```python
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
```
**fibonacci**  
    - it function created using above closure function  

**add, mul and div**  
    - Are simple add, mul div function for demonstrating the counter function  

**cnt**  
    - Global dictionary to keep count of add mul and div function call  

**counter**  
    - Closure function to generate function with not only runs the function but also keep tracks of its count using global cnt dictionary
```python
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
```

**user_counter**  
    - Closure function to generate function with not only runs the function but also keep tracks of its count with user defined dicitionary  
```python
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
```


## 4. Key Learnings

### 4.1 GLOBAL & LOCAL SCOPES
- Scope and namespaces 
- Lexical scope of variable, bindings are stored in names spaces
- Each scopes have their own namespaces 
- Global scope is essentially the module scope. It spans a single file only.
- There is not concept of truly global scope.
- Built-in variables and global variables can be used anywhere inside module

### 4.2 NON LOCAL SCOPES
- We can define functions inside another function.
- The scope which is neither local or global - it is called a non-local scope.
- Can be accessed using keyword nonlocal

### 4.3 CLOSURES & APPLICATIONS
- Tracking a user function call with counter
- Free variables and closure. Function defined inside another function can access the outer (nonlocal) variables.

## 5. References
- [Closures and Decorators in Python](https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6)
- [EPAi Session 8, https://theschoolof.ai/](https://theschoolof.ai/)