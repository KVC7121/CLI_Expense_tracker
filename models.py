from dataclasses import dataclass

@dataclass
class Expense:
    id: int
    amount: float
    category: str
    description: str
    date: str

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Amount: ₹ {self.amount}\n"
            f"Category: {self.category}\n"
            f"Description: {self.description}\n"
            f"Date: {self.date}"
        )