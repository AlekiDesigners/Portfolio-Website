from flask import Response


def test_home(client):
  Response = client.get("/")
  assert Response.status_code == 200
