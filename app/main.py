
import socket
from multiprocessing import Process

from app.urls import router
from app.connection import Connection
from app.settings import ADDRESS, PORT


def main():
    server_socket = socket.create_server((ADDRESS, PORT), reuse_port=True)
    while True:
        conn, addr = server_socket.accept()
        if conn:
            p = Process(target=process_connection, args=(conn, addr))
            p.run()


def process_connection(conn, addr):
    with conn:
        conn_obj = Connection(conn, router)
        conn_obj.read_data()
        conn_obj.set_url()

        response = conn_obj.parse_request()
        conn_obj.send_response(response)


if __name__ == "__main__":
    main()
