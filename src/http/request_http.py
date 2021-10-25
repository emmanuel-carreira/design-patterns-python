import json
import requests

from src.http.http_adapter import HttpAdapter


class RequestHttp(HttpAdapter):
    def post(self, url: str, dados: dict):
        requests.post(url, json=json.dumps(dados))
