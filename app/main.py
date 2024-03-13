
import socket

from app.http_codes import HTTP_200_OK, HTP_404_NOT_FOUND

ADDRESS = "localhost"
PORT = 4221


def main():
    server_socket = socket.create_server((ADDRESS, PORT), reuse_port=True)
    while True:
        conn, addr = server_socket.accept()
        if conn:
            data = conn.recv(4096)
            data = data.split(b" ")
            method, path = data[0], data[1]

            if is_path_valid(path):
                conn.send(HTTP_200_OK)
            else:
                conn.send(HTP_404_NOT_FOUND)
            conn.close()


def is_path_valid(path):
    valid_paths = [b"/"]
    if path in valid_paths:
        return True
    return False


if __name__ == "__main__":
    main()
