"""
The interal database responsible for maintaining the data and internal 
state of the system.

Author: Nicholas Read
"""
from typing import List

from .issue import Issue

class Database:
    """
        The interal database responsible for maintaining the data and internal 
        state of the system.
    """

    __slots__ = ["issues"]
    
    issues: List[Issue]

    def save():
        """Save the database to file."""
        pass

    def load():
        """Loads the database from file."""
        