from dataclasses import dataclass

@dataclass
class Person:
    Name : str
    Address : str
    Interest : str

users = [Person("Example name", "255 Academy St", "Board Games")]
