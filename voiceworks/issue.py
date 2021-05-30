"""
Represents an issue of Voiceworks, comprising many submissions broken 
into categories.

Author: Nicholas Read
"""
from typing import List

from .category import Category

class Issue:
    """
        A collection of Category and CategoryPoetry objects representing 
        all submissions to a Voiceworks issue.
    """

    __slots__ = ["name", "categories"]

    name: str
    categories: List['Category']