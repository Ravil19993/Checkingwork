from ApiCompany import ApiCompany
from time import sleep

base_url = 'https://x-clients-be.onrender.com/'
api = ApiCompany(base_url)


# Получить список всех компаний
def test_all_companies_list():
    response = api.get_list_of_companies(None)
    assert len(response) != 0


# Получить список активных и не активных компаний и проверить, что их сумма
# равна числу всех компаний
def test_active_companies_list():
    resp_all_companies = api.get_list_of_companies(None)
    resp_active_companies = api.get_list_of_companies({"active": True})
    resp_deactive_companies = api.get_list_of_companies({"active": False})
    assert len(resp_all_companies) == len(resp_active_companies) +\
        len(resp_deactive_companies)


# Проверка создания новой организации
def test_add_new_company():
    # Смотрим кол-во имеющихся организаций
    resp_all_companies = api.get_list_of_companies(None)
    len_before = len(resp_all_companies)

    # Тестовые данные 
    name = "Создано в VSCode"
    description = "Описание задано в VSCode"

    # Создаем новую компанию
    resp = api.create_new_company(name, description)
    new_id = resp["id"]

    # Получаем информацию о созданной организации
    new_company = api.get_info_about_company(new_id)

    # Снова смотрим кол-во имеющихся организаций
    resp_all_companies = api.get_list_of_companies(None)
    len_after = len(resp_all_companies)

    # Проверяем, что разница в количестве компаний после и до добавления
    # компании равна 1
    assert len_after - len_before == 1
    # Сверяем заданное и полученное из БД имя
    assert name == new_company["name"]
    # Сверяем заданное и полученное из БД описание
    assert description == new_company["description"]
    # Сверяем статус компании (по умолчанию равен isActive = True)
    assert new_company["isActive"] == True


# Проверка изменения информации о существующей компании
def test_edit():
    # Тестовые данные
    name = "Создано в VSCode"
    description = "Описание задано в VSCode"

    # Создаем новую организацию
    resp = api.create_new_company(name, description)
    new_id = resp["id"]

    # Новые тестовые данные
    changed_name = "Имя изменено тестом"
    changed_description = "Описание изменено тестом"

    edited = api.edit_company(new_id, changed_name, changed_description)

    # Проверяем, что новое имя
    assert changed_name == edited["name"]
    # Проверяем, что новое описание
    assert changed_description == edited["description"]
    # Проверяем, что статус не сменился
    assert edited["isActive"] == True


# Проверка деактивировации компании
def test_deactivate_status():
    # Тестовые данные
    name = "Создано в VSCode"
    description = "Описание задано в VSCode"

    # Создаем новую организацию
    resp = api.create_new_company(name, description)
    new_id = resp["id"]

    # Задаем новый статус = Deactivated
    status = False

    # Меняем статус на Deactivated
    api.change_status(new_id, status)

    # Смотрим статус у компании
    resp = api.get_info_about_company(new_id)
    got_status = resp["isActive"]

    # Проверяем, что статус изменен на False
    assert got_status == False


# Проверка активировации компании
def test_activate_status():
    # Тестовые данные
    name = "Создано в VSCode"
    description = "Описание задано в VSCode"

    # Создаем новую организацию
    resp = api.create_new_company(name, description)
    new_id = resp["id"]

    # Задаем новый статус = Deactivated
    status = False
    api.change_status(new_id, status)

    # Меняем статус на Activated
    status = True
    api.change_status(new_id, status)

    # Смотрим статус у компании
    resp = api.get_info_about_company(new_id)
    got_status = resp["isActive"]

    # Проверяем, что статус изменен на False
    assert got_status == True


def test_delete():
    # Тестовые данные
    name = "Создано в VSCode"
    description = "Описание задано в VSCode"

    # Создаем новую организацию
    created = api.create_new_company(name, description)
    new_id = created["id"]

    # Удаляем созданную организацию
    deleted = api.delete_company(new_id)
    sleep(4)  # Серверу необходимо время для обращения в БД и обновления данных о компании

    # Проверяем, что ID последней созданной компании = ID удаленной компании
    assert new_id == deleted["id"]

    # Проверяем, что название последней созданной компании ==
    # названию удаленной компании
    assert name == deleted["name"]

    # Проверяем, что описание последней созданной компании ==
    # описанию удаленной компании
    assert description == deleted["description"]

    # Проверяем, что ID удаленной компании нет в обновленном списке
    company_list = api.get_list_of_companies(None)
    assert company_list[-1]["id"] != new_id
