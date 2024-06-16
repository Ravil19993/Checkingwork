# Получить список всех сотрудников
# Добавить нового сотрудника
# Получить сотрудника по id
# Изменить информацию о сотруднике
from EmployeePage import Employee
from ApiCompany import ApiCompany
from faker import Faker

fake = Faker("ru_RU")


base_url = 'https://x-clients-be.onrender.com/'
employee = Employee(base_url)
api = ApiCompany(base_url)


# Проверить, что в указанной организации есть пользователь
def test_get_employees():
    name = "Тестовая компания"
    description = "Описание тестовой компании"

    # Создаем организацию + Создаем пользователя в этой организации
    # + Проверяем, что у организации есть созданный сотрудник
    company = api.create_new_company(name, description)
    company_id = company["id"]
    employee_params = {
            "id": 0,  # Зачем здесь id при создании нового пользователя
            "firstName": fake.first_name_male(),
            "lastName": fake.last_name_male(),
            "middleName": fake.middle_name_male(),
            "companyId": company_id,
            "email": fake.email(),
            "url": fake.url(),
            "phone": str(fake.phone_number()),
            "birthdate": "2024-06-14T07:50:03.386Z",
            "isActive": True
        }

    employee.create_employee(employee_params)

    my_params = {'company': str(company_id)}
    employee_list = employee.get_list_of_employees(my_params)
    assert len(employee_list) != 0


def test_create_employee():
    name = "Тестовая компания"
    description = "Описание тестовой компании"

    company = api.create_new_company(name, description)
    company_id = company["id"]

    employee_params = {
            "id": 0,
            "firstName": fake.first_name_male(),
            "lastName": fake.last_name_male(),
            "middleName": fake.middle_name_male(),
            "companyId": company_id,
            "email": fake.email(),
            "url": fake.url(),
            "phone": str(fake.phone_number()),
            "birthdate": "2024-06-14",
            "isActive": True
        }

    employee_id = employee.create_employee(employee_params) # Создали пользователя
    employee_id = employee_id["id"]
    employee_info = employee.get_info_about_employee(employee_id) # Получили данные о пользователе
    
    # Проверки на соответствие данных во всех полях
    assert employee_params["firstName"] == employee_info["firstName"]
    assert employee_params["lastName"] == employee_info["lastName"]
    assert employee_params["middleName"] == employee_info["middleName"]
    assert employee_params["companyId"] == employee_info["companyId"]
    assert employee_params["email"] == employee_info["email"]
    assert employee_params["url"] == employee_info["url"]  # Сервер возвращает ключ avatar_url вместо url
    assert employee_params["phone"] == employee_info["phone"]
    assert employee_params["birthdate"] == employee_info["birthdate"]
    assert employee_params["isActive"] == employee_info["isActive"]


def test_change_employee_info():
    #  Данные по созданию тестовой организации
    name = "Тестовая компания"
    description = "Описание тестовой компании"    

    company = api.create_new_company(name, description)
    company_id = company["id"]

    employee_params = {
            "id": 0,
            "firstName": fake.first_name_male(),
            "lastName": fake.last_name_male(),
            "middleName": fake.middle_name_male(),
            "companyId": company_id,
            "email": fake.email(),
            "url": fake.url(),
            "phone": str(fake.phone_number()),
            "birthdate": "2024-06-14",
            "isActive": True
        }

    employee_id = employee.create_employee(employee_params)  # Создали пользователя
    employee_id = employee_id["id"]  # Вытаскиваем id созданного пользователя
    # для дальнейшего изменения данных о нем

    #  Новые данные по пользователю
    edit_params = {
        "lastName": fake.last_name_male(),
        "email": fake.email(),
        "url": fake.url(),
        "phone": str(fake.phone_number()),
        "isActive": True
    }

    employee.change_info(employee_id, edit_params)  # Внесли изменения
    employee_edited = employee.get_info_about_employee(employee_id)

    # Проверки на соответствие данных во всех полях
    assert edit_params["lastName"] == employee_edited["lastName"]
    assert edit_params["email"] == employee_edited["email"]
    assert edit_params["url"] == employee_edited["url"]  # Сервер возвращает ключ avatar_url вместо url
    assert edit_params["phone"] == employee_edited["phone"]  # Сервер не перезаписывает телефон пользователя
    assert edit_params["isActive"] == employee_edited["isActive"]
    assert employee_params["firstName"] == employee_edited["firstName"]
    assert employee_params["middleName"] == employee_edited["middleName"]
    assert employee_params["companyId"] == employee_edited["companyId"]
    assert employee_params["birthdate"] == employee_edited["birthdate"]
