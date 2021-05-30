"""
Wrapper around request object.

Author: Nicholas Read
"""
from typing import List

from .category import Category
from .submission import Submission

class Request:

    def request_categories() -> List[Category]:
        """Request the Submittable categories."""
        pass

    def request_submissions(category: Category) -> List[Submission]:
        """Request the Submittable submissions for `category`."""
        pass