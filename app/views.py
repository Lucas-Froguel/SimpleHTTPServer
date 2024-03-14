
from app.http_codes import HTTP_STATUS
from app.settings import ENCODE_TYPE


def index(data: bytes, **kwargs) -> (bytes, bytes):
    return HTTP_STATUS.HTTP_200_OK, b""


def echo(data: bytes, **kwargs) -> (bytes, bytes):
    split_data = data.split(b" ")
    url = split_data[1]
    msg = url.replace(b"/echo/", b"")

    response_message = (
        f"Content-Type: text/plain\r\nContent-Length: {len(msg)}\r\n\r\n{msg.decode(ENCODE_TYPE)}\r\n"
    )

    return HTTP_STATUS.HTTP_200_OK, response_message.encode(ENCODE_TYPE)


def user_agent(data: bytes, **kwargs) -> (bytes, bytes):
    split_data = data.split(b"\r\n")

    msg = split_data[2].split(b" ")[1]

    response_message = (
        f"Content-Type: text/plain\r\nContent-Length: {len(msg)}\r\n\r\n{msg.decode(ENCODE_TYPE)}\r\n"
    )

    return HTTP_STATUS.HTTP_200_OK, response_message.encode(ENCODE_TYPE)


def files(data: bytes, directory: str = None, method: str = None):
    split_data = data.split(b" ")
    url = split_data[1]
    file = url.replace(b"/files", b"").decode(ENCODE_TYPE)

    if method == b"GET":
        try:
            with open(directory + file, "r") as fl:
                msg = fl.read()
        except FileNotFoundError:
            return HTTP_STATUS.HTTP_404_NOT_FOUND, b""

        response_message = (
            f"Content-Type: application/octet-stream\r\nContent-Length: {len(msg)}\r\n\r\n{msg}\r\n"
        )

        return HTTP_STATUS.HTTP_200_OK, response_message.encode(ENCODE_TYPE)
    elif method == b"POST":
        content = data.split(b"\r\n\r\n")[1]
        print(content)
        with open(directory + file, "wb") as fl:
            print(content)
            fl.write(content)

        return HTTP_STATUS.HTTP_201_CREATED, b""
