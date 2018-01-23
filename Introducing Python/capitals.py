"""
Sample program for learning to use pdb.
"""

import sys

def process_cities(filename):
    """
    Read line, strip leading and trailing spaces,
    and quit if 'quit' appears in the lowercase
    copy of the line.
    
    Else, split country and capital by comma,
    trim leading and trailing spaces,
    convert the country and capital to title case,
    and print the capital, a comma, and the country.
    """
    
    with open(filename, 'rt') as file:
        for line in file:
            line = line.strip()
            if 'quit' == line.lower():
                return
            country, city = line.split(',')
            city = city.strip()
            country = country.strip()
            print(city.title(), country.title(), sep=',')

if __name__ == '__main__':
    process_cities(sys.argv[1])
