"""
A small class for handling Voicework ids.

Author: Nicholas Read
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class VoiceworkID:
    """
        The submission ID, as understood by Voiceworks. They are comprise
        of a number and an option letter.

        Each unique number corresponds to a unique author. Letters are 
        used to denote multiple submissions from the same author. IDs 
        begin numbering from the start of the category range.

        Non-fiction: [1, 100)
        Poetry: [100, 200)
        Art and comics: [200, 300)
        Fiction: [300, 500)
        Non-fiction pitches: [500, inf)
    """

    __slots__ = ["number", "letter"]
    number: int
    letter: Optional[str]

    def __str__(self) -> str:
        return str(self.number) + self.letter
