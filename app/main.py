
import socket

from app.urls import router
from app.connection import Connection


ADDRESS = "localhost"
PORT = 4221
ENCODE_TYPE = "utf-8"


def main():
    server_socket = socket.create_server((ADDRESS, PORT), reuse_port=True)
    while True:
        conn, addr = server_socket.accept()
        if conn:
            with conn:
                conn_obj = Connection(conn, router)
                conn_obj.read_data()
                conn_obj.set_url()

                response = conn_obj.parse_url()
                conn_obj.send_response(response)


if __name__ == "__main__":
    main()
