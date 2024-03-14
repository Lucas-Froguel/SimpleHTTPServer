
from types import FunctionType


class Router:
    def __init__(self):
        self.urls_and_functions: dict = {}

    def register(self, path: str, view: FunctionType):
        self.urls_and_functions[path] = view

    def get_view(self, path: str):
        return self.urls_and_functions[path]

    def get_urls(self):
        return self.urls_and_functions.keys()

    def is_url_valid(self, path: str):
        return path in self.get_urls()

