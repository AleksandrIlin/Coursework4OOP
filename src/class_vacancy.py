class Vacancy:
    """Класс для обработки вакансий"""

    def __init__(self, name: str, salary, url: str, employer: str, requirement: str):
        self.name = name
        self.url = url
        self.validate_salary(salary)
        self.employer = employer
        self.requirement = requirement

    def validate_salary(self, salary):
        if salary is None:
            self.salary_from = 0
            self.salary_to = 0
        else:
            self.salary_from = salary["from"] if salary["from"] else 0
            self.salary_to = salary["to"] if salary["to"] else 0

    def __str__(self):
        return (
            f"Название: {self.name}\n"
            f"Зарплата: от {self.salary_from} до {self.salary_to}\n"
            f"Ссылка: {self.url}\n"
            f"Название компании: {self.employer}\n"
            f"Требования: {self.requirement}\n"
        )

    def __repr__(self):
        return f"Vacancy({self.name}, {self.salary}, {self.url}, {self.employer}, {self.requirement})"

    def __gt__(self, other):
        return self.salary_to > self.salary_to

    def __lt__(self, other):
        """сортировка"""
        return (self.salary_from, self.salary_to) < (other.salary_from, other.salary_to)
