"""
Skills function practice.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> num_spaces("Balloonicorn is       awesome!")
    8

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    >>> sign_and_parity(3)
    ['Positive', 'Odd']

    >>> sign_and_parity(-2)
    ['Negative', 'Even']

PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""

def hello_world():
    """ Print a message that says Hello World

    >>> hello_world()
    Hello World

    """
    print "Hello World"

def say_hi(name):
    """ Print a message that says Hi <name>, where name is given as an argument

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    """
    print "Hi {}".format(name)


def print_product(num1, num2):
    """ Print the product of two numbers, given as arguments

    >>> print_product(3, 5)
    15

    """

    print num1 * num2

def repeat_string(input_string, num):
    """ Print a string a repeated a number of times, given as arguments

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    """

    print input_string * num

def print_sign(num):
    """ Print a message indicating if a number, given as an input, is less than,
    greater than or equal to zero

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    """

    if num > 0:
        print "Higher than 0"
    elif num < 0:
        print "Lower than 0"
    else:
        print "Zero"


def is_divisible_by_three(num):
    """ Return a boolean based on a number given as an argument. True if the
    number is divsible by three, False otherwise.

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    """

    if num % 3 == 0:
        return True
    else:
        return False

def num_spaces(input_string):
    """ Return the number of spaces in a string given as an input

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> num_spaces("Balloonicorn is       awesome!")
    8

    """

    count_spaces = 0
    for letter in input_string:
        if letter == ' ':
            count_spaces += 1

    return count_spaces


def total_meal_price(sub_total, tip=0.15):
    """ Return the total meal price based on a subtotal given as an argument and
    a tip percentage of .15 unless given as an argument as well

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0

    """

    total_tip = sub_total * tip
    return sub_total + total_tip

def sign_and_parity(num):
    """ Return a list of two items, strings identifying Positive or Negative and
    Even or Odd

    >>> sign_and_parity(3)
    ['Positive', 'Odd']

    >>> sign_and_parity(-2)
    ['Negative', 'Even']

    """

    sign_parity_list = []
    if num > 0:
        sign_parity_list.append("Positive")
    elif num < 0:
        sign_parity_list.append("Negative")
    else:
        sign_parity_list.append("Zero")

    if num % 2 == 0:
        sign_parity_list.append("Even")
    else:
        sign_parity_list.append("Odd")

    return sign_parity_list

def full_title(name, job_title="Engineer"):
    """ Return the person's title and name, which are given as arguments, as one
    string

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    """

    return job_title + " " + name

def write_letter(recipient_name, job_title, sender_name):
    """ Print a greeting given recipient name, job title and sender name as
    arguments

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

    """

    print "Dear " + full_title(recipient_name, job_title) + ", I think you are amazing! Sincerely, " + sender_name


hello_world()
say_hi("Balloonicorn")
print_product(3, 5)
repeat_string("Balloonicorn", 3)
print_sign(3)
print_sign(0)
print_sign(-3)
is_divisible_by_three(12)
is_divisible_by_three(10)
num_spaces("Balloonicorn is awesome!")
total_meal_price(30)
total_meal_price(30, .3)
sign_and_parity(3)
sign, parity = sign_and_parity(-2)

print sign, parity

full_title("Balloonicorn")
full_title("Jane Hacks", "Hacker")
write_letter("Jane Hacks", "Hacker", "Balloonicorn")

###############################################################################

# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".


# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.


# 3. Write a function called 'print_product' that takes two integers and
#    multiplies them together. Print the result.


# 4. Write a function called 'repeat_string' that takes a string and an integer
#    and prints the string that many times


# 5. Write a function called 'print_sign' that takes an integer and prints
#    "Higher than 0" if higher than zero and "Lower than 0" if lower than zero.
#    If the integer is zero, print "Zero".


# 6. Write a function called 'is_divisible_by_three' that takes an integer and
#    returns a boolean (True or False), depending on whether the number is
#    evenly divisible by 3.


# 7. Write a function called 'num_spaces' that takes a sentence as one string
#    and returns the number of spaces.


# 8. Write a function called 'total_meal_price' that can be passed a meal price
#    and a tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip percentage should
#    be optional; if not given, it should default to 15%.


# 9. Write a function called 'sign_and_parity' that takes an integer as an
#    argument and returns two pieces of information as strings --- "Positive"
#    or "Negative" and "Even" or "Odd". The two strings should be returned in
#    a list.
#
#    Then, write code that shows the calling of this function on a number and
#    unpack what is returned into two variables --- sign and parity (whether
#    it's even or odd). Print sign and parity.


###############################################################################

# PART TWO

# 1. Write a function that takes a name and a job title as parameters, making
#    it so the job title defaults to "Engineer" if a job title is not passed
#    in. Return the person's title and name in one string.

# 2. Given a recipient name & job title and a sender name, print the following
#    letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.


###############################################################################

# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
