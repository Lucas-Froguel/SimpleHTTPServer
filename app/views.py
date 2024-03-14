
from app.http_codes import HTTP_STATUS


def index(data: bytes) -> (bytes, bytes):
    response_message = (
        b"Content-Type: text/plain\r\nContent-Length: 0\r\n\r\r\n"
    )

    return HTTP_STATUS.HTTP_200_OK, response_message


def echo(data: bytes) -> (bytes, bytes):
    split_data = data.split(b" ")
    url = split_data[1]
    msg = url.replace(b"/echo/", b"")

    response_message = (
        f"Content-Type: text/plain\r\nContent-Length: {len(msg)}\r\n\r\r\n{msg.decode()}\r\n"
    )

    return HTTP_STATUS.HTTP_200_OK, response_message.encode()

