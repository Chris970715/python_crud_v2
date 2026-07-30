from dataclasses import dataclass

@dataclass
class InputDTO:
    title: str
    description: str
    completed: bool = False

@dataclass
class UpdateInputDTO:
    title: str | None
    description: str | None
    completed: bool | None