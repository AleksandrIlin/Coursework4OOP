import pytest
from src.class_hh_api import HeadHunter


@pytest.fixture
def headhunter_instance():
    return HeadHunter()


def test_get_response(headhunter_instance):
    response = headhunter_instance.get_response("python", 5)
    assert response.status_code == 200


def test_get_vacancies(headhunter_instance):
    vacancies = headhunter_instance.get_vacancies_response("python", 5)
    assert isinstance(vacancies, list)

# def test_get_filter_vacancies(headhunter_instance):
#     filtered_vacancies = headhunter_instance.get_filter_vacancies("python")
#     assert isinstance(filtered_vacancies, list)
#     assert len(filtered_vacancies) > 0
#     for vacancy in filtered_vacancies:
#         assert "name" in vacancy
#         assert "salary_from" in vacancy
#         assert "salary_to" in vacancy
#         assert "salary_currency" in vacancy
#         assert "url" in vacancy
#         assert "employer" in vacancy
#         assert "requirement" in vacancy
#         assert "responsibility" in vacancy
#
# def test_get_filter_vacancies_with_per_page(headhunter_instance):
#     filtered_vacancies = headhunter_instance.get_filter_vacancies("python", per_page=10)
#     assert isinstance(filtered_vacancies, list)
#     assert len(filtered_vacancies) == 10
#     for vacancy in filtered_vacancies:
#         assert "name" in vacancy
#         assert "salary_from" in vacancy
#         assert "salary_to" in vacancy
#         assert "salary_currency" in vacancy
#         assert "url" in vacancy
#         assert "employer" in vacancy
#         assert "requirement" in vacancy
#         assert "responsibility" in vacancy
#
# def test_get_filter_vacancies_empty_result(headhunter_instance):
#     filtered_vacancies = headhunter_instance.get_filter_vacancies("non-existent-job")
#     assert isinstance(filtered_vacancies, list)
#     assert len(filtered_vacancies) == 0