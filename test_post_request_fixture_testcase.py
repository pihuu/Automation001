# post request
import json, requests, jsonpath, pytest

url = 'https://reqres.in/api/users'

json_input = {
    "name": "pikachu",
    "job": "teacher"
}
response = requests.post(url, json_input)
json_output = json.loads(response.text)
print(response)
print(response.text)
print(response.content)


@pytest.fixture()
def create_fixture():
    print('\nbefore testcases')
    yield
    print('\nafter testcases')


def test_post_req1(create_fixture):
    assert response.status_code == 201
    print(json_output['job'])
    assert json_output['job'] == 'teacher'


def test_post_req2(create_fixture):
    print(json_output['name'])
    assert json_output['name'] == 'pikachu'
