
import socket

from app.http_codes import HTTP_200_OK

ADDRESS = "localhost"
PORT = 4221


def main():
    server_socket = socket.create_server((ADDRESS, PORT), reuse_port=True)
    while True:
        conn, addr = server_socket.accept()
        if conn:
            conn.send(HTTP_200_OK)
            conn.close()


if __name__ == "__main__":
    main()
