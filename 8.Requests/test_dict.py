import pytest
empty_dict = {}


football_list = {
    "Число стран": 48,
    "Участники": ["Австралия", "Аргентина", "Армения", "Россия", "Англия"],
    "Страна": "Катар",
    "Награды": {
        "Золотой мяч": "Леонель",
        "Серебрянный мяч": "Мбаппе",
        "Золотая бутса": "Мбаппе",
        "Серебрянная бутса": "Мбаппе",
        "Больше всего голов": {
            "Игрок": "Игорок Килиан Мбаппе - капитан команды",
            "Количество мячей": 8
        }
    }
}


def test_empty_dict():
    assert len(empty_dict) == 0


def test_read_value():
    count = football_list["Страна"]
    assert count == "Катар"


def test_write_value():
    len_before = len(football_list)
    winner = football_list["Победитель"] = "Аргентина"
    print(football_list)
    assert winner == "Аргентина"
    assert len(football_list) == len_before + 1


def test_read_list():
    england = football_list["Участники"][4]
    assert england == "Англия"


def test_read_dict():
    player = football_list["Награды"]["Больше всего голов"]["Игрок"]
    assert player == "Игорок Килиан Мбаппе - капитан команды"


def test_save_dict():
    awards = football_list["Награды"]
    total_goals = awards["Больше всего голов"]["Количество мячей"]
    assert total_goals == 8


def test_read_error():
    with pytest.raises(KeyError):
        value = empty_dict["key"]


#кейс, когда возможно нет какой-то информации в словаре, берем за основу нами заданную величину
def test_get_error():
    value = empty_dict.get("key", "дефолтное значние, если ничего не найдет")
    assert value == "дефолтное значние, если ничего не найдет"
