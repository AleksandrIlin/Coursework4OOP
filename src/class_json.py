import json
from abc import ABC, abstractmethod

from src.class_vacancy import Vacancy


class FileAbstractClass(ABC):
    @abstractmethod
    def write_data(self, vacancies):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JSONSaver(FileAbstractClass):
    def __init__(self, filename="vacancies.json"):
        self.filename = f"../data/{filename}"

    def write_data(self, vacancies):
        with open(self.filename, "w") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def get_vacancies(self) -> list:
        with open(self.filename) as f:
            data = json.load(f)
        vacancies = []
        for vacancy in data:
            vacancies.append(Vacancy(
                name=vacancy['name'],
                salary=vacancy['salary'],
                url=vacancy['alternate_url'],
                employer=vacancy['employer']['name'],
                requirement=vacancy["snippet"]['requirement']
            ))
        return vacancies

    def delete_vacancy(self):
        """Метод удаления данных из файла"""
        list_vacancies_del = []
        list_del = json.dumps(list_vacancies_del, ensure_ascii=False)
        with open("../data/my_vacancies.json", "w", encoding="utf8") as f:
            f.write(list_del)
