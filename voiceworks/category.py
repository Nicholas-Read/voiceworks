"""
Represents an issue of Voiceworks, comprising many submissions broken 
into categories.

Author: Nicholas Read
"""
from typing import List
import submittable

from .submission import Submission



class Category:
    """
        Represents a category of submissions for fiction, non-fiction, 
        non-fiction pitches, and comic and art, where each submission
        is unique.
    """
    __slots__ = ["name", "submissions"]

    name: str
    submissions: List['Submission']

    def __init__(self, name: str):
        """
            A Voiceworks category for submissions.

            Parameters
            ----------
            name : str
                The category name, such as fiction, non-fiction or poetry.
        """
        self.name = name
        self.submissions = []

    def insert(submission: 'submittable.Submission') -> bool:
        """
            Extends the container by unpacking `submission` into 
            voiceworks.Submission objects before adding them.

            Since each submission in a Category is unique, the insert
            operation checks if items corresponding to `submission` 
            already exist in the Category and if so, do not extend the
            container.

            Parameters
            ----------
            submission: voiceworks.Submission
                Submission to insert.

            Returns
            -------
            True if insertion is sucessful.
        """
        pass
    
