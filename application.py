import os
import sys

#   This package is a calculator that takes any mathematical(infex) expression and converts it 
# to prefix, then uses that form to calculate the result, in case of letters for operands it just outputs
# the prefix without calculating the result
# 
# It can handle a variety of odd cases which you'll see as you follow the documentation


# This is the main file of this package, all it does is add the path for dependency packages ./vendor
# to the system path, and runs the window module as the parent  

# Add vendor directory to module search path
parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, 'vendor')

sys.path.append(vendor_dir)

import lib.window  


# ~~~~~~~~IMPORTANT~~~~~~~~
### please note that individual files wont work as standalone scripts
### unless you remove all the '.' from the import statments

# next file => ./lib/window.py