from src.class_hh_api import HeadHunter
from src.utils import get_salary, get_vacancies_by_salary
from src.class_json import JSONSaver


def main() -> None:
    """Главная функция работы с пользователем"""
    hh = HeadHunter()
    print('Получаем вакансии с сайта')
    vacancies = hh.get_vacancies('junior python', 15)
    print('Сохраняем вакансии в файл')
    saver = JSONSaver()
    saver.write_data(vacancies)
    print('Добрый день! С помощью этого приложения поиск вакансий на hh.ru станет намного проще.')
    min_salary, max_salary = get_salary()
    vacancies = get_vacancies_by_salary(min_salary, max_salary)
    counter_vacancy = 0
    for vacancy in vacancies:
        counter_vacancy += 1
        print(f"№ вакансии: {counter_vacancy}")
        print(vacancy)


main()
