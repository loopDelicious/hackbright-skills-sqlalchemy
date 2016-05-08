"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
# Brand.query.get(1)

# # Get all models with the **name** Corvette and the **brand_name** Chevrolet.
# Model.query.filter(Model.name=='Corvette', Brand.name=='Chevrolet').all()

# # Get all models that are older than 1960.
# Model.query.filter(Model.year <1960).all()

# # Get all brands that were founded after 1920.
# Brand.query.filter(Brand.founded > 1920).all()

# # Get all models with names that begin with "Cor".
# Model.query.filter(Model.name.like('Cor%')).all()

# # Get all brands that were founded in 1903 and that are not yet discontinued.
# Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()

# # Get all brands that are either 1) discontinued (at any time) or 2) founded 
# # before 1950.
# Brand.query.filter((Brand.discontinued != None)|(Brand.founded < 1950)).all()

# # Get any model whose brand_name is not Chevrolet.
# Model.query.filter(Model.brand_name != 'Chevrolet').first()

# Fill in the following functions. (See directions for more info.)
def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    # returns a list of all objects fulfilling the filter criteria
    cars = db.session.query(Model.name,
                            Model.brand_name,
                            Brand.headquarters).filter(Model.year == year, Model.brand_name == Brand.name).all()
    # print cars

    for car in cars:
        print car.name, car.brand_name, car.headquarters

# get_model_info(1909)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    # returns list of tuples of brands and models
    # GROUP_BY the same fields that I am SELECTing from
    brands = db.session.query(Model.brand_name, Model.name).group_by('brand_name', 'name').all()

    # iterate through list to print brands and models
    for brand in brands:
        print brand.brand_name, brand.name

# get_brands_summary()

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
    # The returned value is a record in the brands table where the name equals 'Ford'.  The datatype 
    # is an object and the location of the object in memory.


# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

    # An association table is a middle table that references and links 2 other tables. 
    # It manages a many to many relationship, by acting as the interface and relaying a many to one relationship
    # and a one to many relationship, where the association table holds the one value in between 2 other tables.

# -------------------------------------------------------------------
# Part 3
# Design a function in python that takes in any string as parameter, and returns a list of objects that are brands whose name contains or is equal to the input string.
# Design a function that takes in a start year and end year (two integers), and returns a list of objects that are models with years that fall between the start year (inclusive) and end year (exclusive).

def search_brands_by_name(mystr):
  
    # escape string formatter % to display wildcard % with TWO % symbols (%%)
    brands = Brand.query.filter(Brand.name.like('%%%s%%' % mystr)).all()
    print brands

# search_brands_by_name('ord')

def get_models_between(start_year, end_year):
    
    models = Model.query.filter(Model.year > start_year, Model.year <= end_year).all()
    print models

# get_models_between(1905, 1955)
