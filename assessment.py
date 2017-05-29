"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

"""

###############################################################################

# PART ONE: Write your own function declarations.

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.

#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.

#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', I'd like to visit 'town name here'!" depending on what the function
#        from part (a) evaluates to.

###############################################################################

# PART TWO

#    (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "raspberry", or
#        "blackberry."

#    (b) Write another function, shipping_cost(), which calculates shipping
#        cost by taking a fruit name as a string and calling the `is_berry()`
#        function within the `shipping_cost()` function. Your function should
#        return 0 if is_berry() == True, and 5 if is_berry() == False.

#    (c) Make a function that takes in a number and a list of numbers. It should
#        return a new list containing the elements of the input list, along with
#        given number, which should be at the end of the new list.

#    (d) Write a function calculate_price to calculate an item's total cost by
#        adding tax, and any fees required by state law.

#        Your function will take as parameters (in this order): the base price of
#        the item, a two-letter state abbreviation, and the tax percentage (as a
#        two-digit decimal, so, for instance, 5% will be .05). If the user does not
#        provide a tax rate it should default to 5%.

#        CA law requires stores to collect a 3% recycling fee, PA requires a $2
#        highway safety fee, and in MA, there is a Commonwealth Fund fee of $1 for
#        items with a base price under $100 and $3 for items $100 or more. Fees are
#        added *after* the tax is calculated.

#        Your function should return the total cost of the item, including tax and
#        fees.

def is_hometown(town_name):
    """ Determine if a town name given as an argument is my hometown

    >>> is_hometown("Lake Forest")
    True

    >>> is_hometown("San Francisco")
    False

    """

    if town_name == "Lake Forest":
        return True
    else:
        return False

def full_name(first_name, last_name):
    """ Determine if a town name given as an argument is my hometown

    >>> full_name("Meghan", "Khurana")
    'Meghan Khurana'

    """

    return first_name + " " + last_name

def greeting(first_name, last_name, hometown):
    """ Display a greeting and determine if from the same hometown

    >>> greeting("Meghan", "Khurana", "Lake Forest")
    Hi, Meghan Khurana, we're from the same place!


    >>> greeting("Elenore", "Rigby", "London")
    Hi, Elenore Rigby, I'd like to visit London!

    """

    name = full_name(first_name, last_name)
    if is_hometown(hometown):
        print "Hi, {}, we're from the same place!".format(name)
    else:
        print "Hi, {}, I'd like to visit {}!".format(name, hometown)



def is_berry(fruit):
    """Determines if fruit is a berry

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    """

    if fruit == "strawberry" or fruit == "raspberry" or fruit == "blackberry":
        return True
    else:
        return False


def shipping_cost(fruit):
    """Calculates shipping cost of fruit

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    """

    if is_berry(fruit):
        return 0
    else:
        return 5


def append_to_list(lst, num):
    """Returns a new list consisting of the old list with the given number
       added to the end.

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    """

    lst.append(num)

    return lst


def calculate_price(base_price, state_abbreviation, tax_rate=0.05):
    """Calculate total price of an item, figuring in state taxes and fees.

    >>> calculate_price(40, "CA")
    43.26

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0.0)
    150.0

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

    """

    tax_cost = base_price * tax_rate

    if state_abbreviation == "CA":
        updated_cost = base_price + tax_cost
        # include 3% recycling fee in total cost
        recycling_fee = updated_cost * .03
        return base_price + tax_cost + recycling_fee
    elif state_abbreviation == "NM":
        return base_price + tax_cost
    elif state_abbreviation == "OR":
        return base_price + tax_cost
    elif state_abbreviation == "PA":
        highway_safety_fee = 2
        return base_price + tax_cost + highway_safety_fee
    elif state_abbreviation == "MA":
        if base_price < 100:
            commonwealth_fee = 1
        else:
            commonwealth_fee = 3
        return base_price + tax_cost + commonwealth_fee

# is_hometown("Lake Forest")
# is_hometown("San Francisco")
# full_name("Meghan", "Khurana")
# greeting("Meghan", "Khurana", "Lake Forest")
# greeting("Elenore", "Rigby", "London")

# is_berry("blackberry")
# is_berry("durian")
# shipping_cost("blackberry")
# shipping_cost("durian")
# append_to_list([3, 5, 7], 2)
# calculate_price(40, "CA")
# calculate_price(400, "NM")
# calculate_price(150, "OR", 0.0)
# calculate_price(60, "PA")
# calculate_price(38, "MA")
# calculate_price(126, "MA")

###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own.

#    (a) Make a new function that takes in a list and any number of additional
#        arguments, appends them to the list, and returns the entire list. Hint: this
#        isn't something we've discussed yet in class; you might need to google how to
#        write a Python function that takes in an arbitrary number of arguments.

#    (b) Make a new function with a nested inner function.
#        The outer function will take in a word.
#        The inner function will multiply that word by 3.
#        Then, the outer function will call the inner function.
#        Print the output as a tuple, with the original function argument
#        at index 0 and the result of the inner function at index 1.

#        Example:

#        >>> outer("Balloonicorn")
#        ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


###############################################################################

def add_items_to_list(lst, *args):
    """ Return a list that is taken in as a parameter that adds an arbitrary
    number of things to the list given as arguments as well

    >>> add_items_to_list([1, 2, 3], 4, 5, 6, 7, 8)
    [1, 2, 3, 4, 5, 6, 7, 8]

    """

    for thing in args:
        lst.append(thing)

    return lst


def word_multiplier_outer(word):
    """ The outer function will take in a word. The inner function will multiply
        that word by 3. Then, the outer function will call the inner function.
        Print the output as a tuple, with the original function argument at index
        0 and the result of the inner function at index 1.

        >>> word_multiplier_outer("Balloonicorn")
        ('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')

    """

    print (word, word_multiplier_inner(word))


def word_multiplier_inner(word):
    """ The outer function will take in a word. The inner function will multiply
        that word by 3. Then, the outer function will call the inner function.
        Print the output as a tuple, with the original function argument at index
        0 and the result of the inner function at index 1.

        >>> word_multiplier_inner("Balloonicorn")
        'BalloonicornBalloonicornBalloonicorn'


    """
    return word * 3


# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
