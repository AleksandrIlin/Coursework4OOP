class Vacancy:
    """Класс для обработки вакансий"""

    def __init__(self, name: str, salary: dict, url: str, employer: str, requirement: str):
        if not isinstance(salary, dict):
            raise TypeError("Заработная плата должна быть словарем")
        self.name = name
        self.url = url
        self.salary = salary
        self.employer = employer
        self.requirement = requirement

    def __str__(self):
        return (
            f"Название: {self.name}\n"
            f"Зарплата: от {self.salary["from"]} до {self.salary["to"]} {self.salary["currency"]}\n"
            f"Ссылка: {self.url}\n"
            f"Название компании: {self.employer}"
            f"Требования: {self.requirement}\n"
        )

    def __repr__(self):
        return f"Vacancy({self.name}, {self.salary}, {self.url}, {self.employer}, {self.requirement})"

    def __gt__(self, other):
        return self.salary["to"] > self.salary["to"]

    def __lt__(self, other):
        return self.salary["to"] < self.salary["to"]
