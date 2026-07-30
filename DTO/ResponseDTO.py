from dataclasses import dataclass

@dataclass
class SelectAllResponseDTO:
    id: int
    title: str
    description: str
    completed: bool
