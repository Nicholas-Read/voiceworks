"""
A function that fills out and attaches a coversheet to a submission file.

Author: Nicholas Read
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .submission import Submission

def attach_generic_coversheet(submission: 'Submission'):
    """
        Fills in and attaches the generic Voiceworks coversheet to the
        associated file in `submission`.
    """
    pass

def attach_poetry_coversheet(submission: 'Submission'):
    """
        Fills in and attaches the poetry Voiceworks coversheet to the
        associated file in `submission`.
    """
    pass