class DigitalVideoDisc:
    def __init__(self, title, category, director, length, cost):
        self.title = title
        self.category = category
        self.director = director
        self.length = length
        self.cost = cost

    def __str__(self):
        return (
            f"DVD - {self.title} - {self.category} - {self.director} - "
            f"{self.length} min: {self.cost:.2f} $"
        )
