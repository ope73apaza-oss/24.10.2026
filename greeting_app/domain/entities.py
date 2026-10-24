from dataclasses import dataclass

@dataclass
class Person:
    name: str

    def format_greeting(self) -> str:
        cleaned_name = self.name.strip().title()
        return f"Hola {cleaned_name}, buenas tardes"