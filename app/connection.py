
from socket import socket

from app.router import Router
from app.http_codes import HTTP_STATUS


class Connection:
    def __init__(self, con: socket, router: Router):
        self.router = router
        self.http_status = HTTP_STATUS

        self.conn = con
        self.data: bytes = None
        self.split_data: [bytes] = None
        self.url: bytes = None
        self.method: bytes = None

    def read_data(self) -> None:
        self.data = self.conn.recv(4096)
        self.split_data = self.data.split(b" ")

    def set_url(self) -> None:
        self.method, self.url = self.split_data[0], self.split_data[1]

    def parse_request(self):
        split_url = self.url.split(b"/")

        if not self.router.is_url_valid(split_url[1].decode()):
            status = HTTP_STATUS.HTTP_404_NOT_FOUND
            body = b""
        else:
            status, body = self.router.get_view(split_url[1].decode())(self.data)

        response = status + body + b"\r\n"

        return response

    def send_response(self, response: bytes) -> None:
        self.conn.send(response)
