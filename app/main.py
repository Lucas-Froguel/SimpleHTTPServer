
import socket
from threading import Thread
from argparse import ArgumentParser

from app.urls import router
from app.connection import Connection
from app.settings import ADDRESS, PORT


def main(arg):
    server_socket = socket.create_server((ADDRESS, PORT), reuse_port=True)
    while True:
        conn, addr = server_socket.accept()
        if conn:
            p = Thread(target=process_connection, args=(conn, addr, arg), daemon=True)
            p.start()


def process_connection(conn, addr, arg):
    with conn:
        conn_obj = Connection(conn, router)
        conn_obj.read_data()
        conn_obj.set_url()

        response = conn_obj.parse_request(arg=arg)
        conn_obj.send_response(response)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--directory", dest="directory")
    args = parser.parse_args()

    arg = {"directory": args.directory}

    main(arg)
