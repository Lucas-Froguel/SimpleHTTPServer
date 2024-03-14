
from dataclasses import dataclass


@dataclass
class HTTP_STATUS:
    HTTP_200_OK = b"HTTP/1.1 200 OK\r\n"
    HTTP_404_NOT_FOUND = b"HTTP/1.1 404 NOT FOUND \r\n"
