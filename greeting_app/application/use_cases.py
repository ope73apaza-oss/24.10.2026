from greeting_app.domain.entities import Person

class GreetPersonUseCase:
    def execute(self, name: str) -> str:
        if not name or not name.strip():
            raise ValueError("El nombre no puede estar vacío.")

        person = Person(name=name)
        return person.format_greeting()