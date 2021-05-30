"""
A Voicework submission, including the file.

Author: Nicholas Read
"""
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .voiceworks_id import VoiceworkID

@dataclass
class Submission:
    """A submission to Voiceworks."""

    __slots__ = ["author", "age", "title", "voiceworks_id"]

    author: str
    age: int
    title: str
    voiceworks_id: 'VoiceworkID'
