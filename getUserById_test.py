import json

import requests


def test_getUserById():
    response = requests.get("https://reqres.in/api/users/1")
    assert response.status_code == 200
    pretty_json = json.loads(response.text)
    print(json.dumps(pretty_json, indent=2))
