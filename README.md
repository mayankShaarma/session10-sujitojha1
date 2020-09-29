# session10-sujitojha1, Tuples and Named Tuples
TSAI EPAi Session 10 Assignment

## 1. Objective: Tuple and named tuples

- Use Faker library to get 10000 random profiles. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age and average age (add proper doc-strings).
- Do the same thing above using a dictionary. Prove that namedtuple is faster.
- Create a fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. - Calculate and show what value stock market started at, what was the highest value during the day and where did it end. Make sure your open, high, close are not totally random. You can only use namedtuple.
- Add the notebook as well to your github where logs can be visible. 

- No readme or no docstring for each function, or no test cases, 0. Write test cases to check boundary conditions that might cause your code to fail. 

## 2. Notebook & Results

[session10_notebook_v1.ipynb](session10_notebook_v1.ipynb)

## 3. Documentation for functions


**Faker & Profile** :  
    - Faker python library to generate fake profile
    - Faker object have fake profile and fake company
    - Updated the profile's doctring namedtuple
    - test case to check docstring are updated
```python
from faker import Faker

# Loading an Faker object
faker = Faker()

# Fake profile named tupple
profile = namedtuple("Fake_Profile", sorted(faker.profile().keys()))
profile.__doc__ = "Fake Profile Created using Faker library"
profile.address.__doc__ = "Permanent Address"
profile.birthdate.__doc__ = "Birth Date"
profile.blood_group.__doc__ = "Blood Group e.g. A+,AB+, O,O+"
profile.company.__doc__ = "Company"
profile.current_location.__doc__ = "Current Location in Latitude and Longitude"
profile.job.__doc__ = "Job Title"
profile.mail.__doc__ = "email address"
profile.name.__doc__ = "Name"
profile.residence.__doc__ = "Residential Address"
profile.sex.__doc__ = "Sex"
profile.ssn.__doc__ = "Social Security Number"
profile.username.__doc__ = "Username"
profile.website.__doc__ = "Website"
```

**namedtuple** :  
    - Created 10000 profiles and 100 companies using namedtuple  
    - Used dictionary to make these large named entities  
```python
# Created 10000 profile dict using namedtuple - profile
profiles_dict_temp = {f"profile_{i}":profile(**faker.profile()) for i in range(10000)}

# Created 10000 people named tuple using inside namedtupple - profile
fake_profiles = namedtuple("Fake_Profiles", sorted(profiles_dict_temp))
fake_profiles_tupple = fake_profiles(**profiles_dict_temp)

# Created 10000 profile dict using dictionary - profile
profiles_dict = {key:value._asdict()for key,value in profiles_dict_temp.items()}

# Created 100 profile dict using namedtuple - faker_company_stock_data
company_dict_temp = {f"company_{i}":faker_company_stock_data() for i in range(100)}

# Created 100 people named tuple using inside namedtupple - faker_company_stock_data
company_stock_market = namedtuple("CompanyStockMarket", sorted(company_dict_temp))
company_stock_market_tupple = company_stock_market(**company_dict_temp)
```
**largest_blood_type**  
    - Function to find the largest blood type  
    - Used Counter from collections to convert a list to dictory of unique counts  
```python
def largest_blood_type(profiles_tpl,profiles_dict):
    """ Find out the largest blood type in given profiles

    Returns:
        Performance for 200x times
    """


    start = perf_counter()
    for i in range(200):
        blood_group_list = [value['blood_group'] for value in profiles_dict.values()]
        blood_group_summary = Counter(blood_group_list)
        Max_blood_group = max(blood_group_summary, key=blood_group_summary.get) 

    elapsed_dict = (perf_counter() - start)/100
    print(f'Dictionary Results\nLargest blood group is {Max_blood_group} and average of 200 run it took {elapsed_dict*1000:4.2f} ms')


    start = perf_counter()
    for i in range(200):
        blood_group_list = [i.blood_group for i in profiles_tpl]
        blood_group_summary = Counter(blood_group_list)
        Max_blood_group = max(blood_group_summary, key=blood_group_summary.get) 

    elapsed_tpl = (perf_counter() - start)/100
    print(f'Named Tuple Results\nLargest blood group is {Max_blood_group} and average of 200 run it took {elapsed_tpl*1000:4.2f} ms')

    return elapsed_tpl,elapsed_dict
```

**mean_current_location**  
    - Function to calculate mean latitude and longitude from 10000 fake profiles  
    - Used reduce function to get sum of latitude and longitude and then dividing by length
```python
def mean_current_location(profiles_tpl,profiles_dict):
    """ Calculates the mean of current location for all profiles

    Returns:
        Performance for 200x times
    """

    start = perf_counter()
    for i in range(200):
        Latitude,Longitude = reduce(lambda prev,next: (prev[0]+next[0],prev[1]+next[1]),[i['current_location'] for i in profiles_dict.values()],(0,0))
        Latitude,Longitude = Latitude/10000,Longitude/10000

    elapsed_dict = (perf_counter() - start)/200
    print(f'Dictionary Results\nMean location: Latitude = {Latitude}, Longitude = {Longitude} and average of 200 run it took {elapsed_dict*1000:4.2f} ms')

    start = perf_counter()
    for i in range(200):
        Latitude,Longitude = reduce(lambda prev,next: (prev[0]+next[0],prev[1]+next[1]),[i.current_location for i in profiles_tpl],(0,0))
        Latitude,Longitude = Latitude/10000,Longitude/10000

    elapsed_tpl = (perf_counter() - start)/200
    print(f'Named Tuple Results\nMean location: Latitude = {Latitude}, Longitude = {Longitude} and average of 200 run it took {elapsed_tpl*1000:4.2f} ms')

    return elapsed_tpl,elapsed_dict
```
**faker_company_stock_data**  
    - Create fake stock company data for 100 companies
    - Used random function to generate 10 day training value in a range of mean + std (+/-10%)
    - Then selecting the open -> first, high -> max, close -> end values
```python
def faker_company_stock_data():
    """Create fake company data with stock open, high and close for a day
    100 companies with random stock prices
    Return:
        Named tuple with company stock exchange
    """
    CompanyStockData = namedtuple('CompanyStockData',"Company_Name Symbol Open High Close")

    # Get company name from Faker
    fake_company_name = faker.company()

    # Set the stock value from Rs. 50 to Rs. 5000 randomly
    min_stock_val=50
    max_stock_val = 5000
    stock_value = (random.randint(0,100)*(max_stock_val-min_stock_val)/100 + min_stock_val)

    # Set the interday change between -10% to +10%
    min_change_val = -10
    max_change_val = 10

    # Random day tranding values created
    day_trading = [stock_value + stock_value/100*random.randint(0,100)*(max_change_val-min_change_val)/100 + min_change_val for i in range(10)]

    fake_company = CompanyStockData(Company_Name=fake_company_name,
                                    Symbol=fake_company_name[0:4].upper(),
                                    Open=day_trading[0], 
                                    High=max(day_trading),
                                    Close=day_trading[-1])
    
    return fake_company

stock_market_status()
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

### 4.1 TUPLES AS A DATA STRUCTURE

### 4.2 NAMED TUPLES

### 4.3 NAMED TUPLES - MODIFYING AND EXTENDING

### 4.3 NAMED TUPLES - DOCSTRING AND DEFAULT VALUES

## 5. References
- [Pythonic way to convert dictory to named tuple](https://stackoverflow.com/questions/43921240/pythonic-way-to-convert-a-dictionary-into-namedtuple-or-another-hashable-dict-li)
- [EPAi Session 10, https://theschoolof.ai/](https://theschoolof.ai/)