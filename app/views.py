
from app.http_codes import HTTP_STATUS
from app.settings import ENCODE_TYPE


def index(data: bytes) -> (bytes, bytes):
    return HTTP_STATUS.HTTP_200_OK, b""


def echo(data: bytes) -> (bytes, bytes):
    split_data = data.split(b" ")
    url = split_data[1]
    msg = url.replace(b"/echo/", b"")

    response_message = (
        f"Content-Type: text/plain\r\nContent-Length: {len(msg)}\r\n\r\n{msg.decode(ENCODE_TYPE)}\r\n"
    )

    return HTTP_STATUS.HTTP_200_OK, response_message.encode(ENCODE_TYPE)


def user_agent(data: bytes) -> (bytes, bytes):
    split_data = data.split(b"\r\n")

    msg = split_data[2].split(b" ")[1]

    response_message = (
        f"Content-Type: text/plain\r\nContent-Length: {len(msg)}\r\n\r\n{msg.decode(ENCODE_TYPE)}\r\n"
    )

    return HTTP_STATUS.HTTP_200_OK, response_message.encode(ENCODE_TYPE)
