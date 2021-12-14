from ApiHelper import ApiHelper
from Utils import generate_random_str_or_num, check_string_in_dict

from pytest import fixture


@fixture
def prepare_user_payload() -> dict:
    return {"name": f"{generate_random_str_or_num()}", "id": f"{generate_random_str_or_num('n')}"}


# description : the test creates new user and validate that response code is 200
# expected result: 200
# actual result: 200
def test_create_user(prepare_user_payload):
    resp = ApiHelper().create_user(payload=prepare_user_payload)
    assert resp.status_code == 200, f"{resp.text}"


# description : the test creates user then try to create another user with same payload
# the database should not contain duplicated records (from my point of view)
# expected result : response code 400
# DEFECT 1 : actual response is 200
def test_duplicate_user_records(prepare_user_payload):
    payload = prepare_user_payload
    ApiHelper().create_user(payload=payload)
    resp2 = ApiHelper().create_user(payload=payload)
    assert resp2.status_code == 400, f"{resp2.text}"


# description : the test creates new user and then uses get api to get the created user
# the test validates that response code is 200
# the test also validate that get request returns correct data in response
def test_get_user(prepare_user_payload):
    payload = prepare_user_payload
    ApiHelper().create_user(payload=payload)
    resp = ApiHelper().get_user(payload["id"])
    assert resp.status_code == 200, f"{resp.text}"
    assert check_string_in_dict(resp.json(), payload["id"])
    assert check_string_in_dict(resp.json(), payload["name"])


# description : the test validate that when giving id that does not exist in DB we get error 404
# the test also validate that we get informative error msg
def test_get_with_non_existent_user(prepare_user_payload):
    resp = ApiHelper().get_user(prepare_user_payload["id"])
    assert resp.status_code == 404, f"{resp.text}"
    assert resp.text == "user not found"


# description : the test creates new user then edit the name value
# the test validate that response code is 200
# then using get api we validate that data is actually changed
# DEFECT 2 : the name is not actually changed
def test_edit_user(prepare_user_payload):
    payload = prepare_user_payload
    ApiHelper().create_user(payload)
    resp = ApiHelper().edit_user(payload={"name": "Husam"}, user=payload["id"])
    assert resp.status_code == 200, f"{resp.text}"
    resp = ApiHelper().get_user(payload["id"])
    assert resp.json()['name'] == "Husam"


def test_get_all_users():
    resp = ApiHelper().get_all_users()
    assert resp.status_code == 200, f"{resp.text}"


# description : the test creates new user then delete it
# the test validate that response code is 200
# DEFECT 3 : actual response is 500
# then we use get method to validate the user does not exist after deleting him
def test_delete_user():
    payload = prepare_user_payload
    ApiHelper().create_user(payload)
    resp = ApiHelper().delete_user(payload["id"])
    assert resp.status_code == 200, f"{resp.text}"
    resp = ApiHelper().get_user(payload["id"])
    assert resp.status_code == 404, f"{resp.text}"
