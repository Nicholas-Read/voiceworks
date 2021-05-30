"""
Package for Submittable API Python interface.

Author: Nicholas Read
"""

# No within-package dependencies
from .category import Category
from .submission import Submission

# Depend on category and submission
from .request import Request