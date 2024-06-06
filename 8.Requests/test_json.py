import json
company_json = """
{
    "id": 111,
    "isActive": true,
    "createDateTime": "2024-04-05T17:30:00.713Z",
    "lastChangedDateTime": "2024-04-05T17:30:00.713Z",
    "name": "Барбершоп 'Цирюльникъ'",
    "description": "Крутые стрижки для крутых шишек"
    }
"""

company_list_json = """
[
    {
    "id": 111,
    "isActive": true,
    "createDateTime": "2024-04-05T17:30:00.713Z",
    "lastChangedDateTime": "2024-04-05T17:30:00.713Z",
    "name": "Барбершоп 'Цирюльникъ'",
    "description": "Крутые стрижки для крутых шишек"
    },
    {
    "id": 112,
    "isActive": true,
    "createDateTime": "2024-04-05T17:30:00.713Z",
    "lastChangedDateTime": "2024-04-05T17:30:00.713Z",
    "name": "Кондитерская Профи-троли",
    "description": "Сладко и точка"
    },
    {
    "id": 113,
    "isActive": true,
    "createDateTime": "2024-04-05T17:30:00.713Z",
    "lastChangedDateTime": "2024-04-05T17:30:00.713Z",
    "name": "Муж на час",
    "description": "Помощь в делах"
    }
]
"""


def test_parsed_json():
    company = json.loads(company_json)
    assert company["id"] == 111


def test_parsed_list_companis():
    list_companies = json.loads(company_list_json)
    assert list_companies[1]["name"] == "Кондитерская Профи-троли"
