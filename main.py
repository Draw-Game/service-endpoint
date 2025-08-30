import socket
import threading

connections = {}

def main():
    print ("YAY")
    # Change to environment variables?
    address = ("0.0.0.0", 8008)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(address)
    server.listen(1)

    while True:
        connection, address = server.accept()

        connections[connection] = None

        client_thread = threading.Thread(target=client_router, args=(connection,))
        client_thread.start()


def client_router(conn):
    match (connections[conn]):
        case None:
            pass
        case "Private Lobby":
            pass

if __name__ == "__main__":
    main()

