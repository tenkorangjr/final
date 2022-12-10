
class NumberOfVisits:

    def __init__(self) -> None:
        self.num = 0

    def get_visit(self):
        """Return the number of times a scene has been visited"""
        return self.num

    def another_visit(self):
        """Mutates the number of times a scene was visited"""
        self.num += 1

    def __str__(self):
        """Function for polymorphism"""

        return str(self.num)
