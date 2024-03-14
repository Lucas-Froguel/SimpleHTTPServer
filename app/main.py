
import socket
from threading import Thread

from app.urls import router
from app.connection import Connection
from app.settings import ADDRESS, PORT


def main():
    server_socket = socket.create_server((ADDRESS, PORT), reuse_port=True)
    while True:
        conn, addr = server_socket.accept()
        if conn:
            p = Thread(target=process_connection, args=(conn, addr), daemon=True)
            p.start()


def process_connection(conn, addr):
    with conn:
        conn_obj = Connection(conn, router)
        conn_obj.read_data()
        conn_obj.set_url()

        response = conn_obj.parse_request()
        conn_obj.send_response(response)


if __name__ == "__main__":
    main()
