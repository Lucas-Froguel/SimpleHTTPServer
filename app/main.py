
import socket

from app.http_codes import HTTP_200_OK, HTP_404_NOT_FOUND
from app.urls import valid_urls

ADDRESS = "localhost"
PORT = 4221
ENCODE_TYPE = "utf-8"


def main():
    server_socket = socket.create_server((ADDRESS, PORT), reuse_port=True)
    while True:
        conn, addr = server_socket.accept()
        if conn:
            data = conn.recv(4096)
            data = data.split(b" ")
            method, url = data[0], data[1]
            msg = url.split(b"/")[-1]

            conn.send(HTTP_200_OK + build_response(msg))
            conn.close()


def is_url_valid(url: bytes) -> bool:
    if url in valid_urls:
        return True
    return False


def build_response(message: bytes) -> bytes:
    response_message = (
        f"Content-Type: text/plain\r\nContent-Length: {len(message)}\r\n\r\r\n{message.decode(ENCODE_TYPE)}\r\n"
    )

    return response_message.encode(ENCODE_TYPE)


if __name__ == "__main__":
    main()
