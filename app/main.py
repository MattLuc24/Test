import socket


def main():
    print("Logs from your program will appear here!")
    
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    client_socket, _ = server_socket.accept()  # wait for client
    client_socket.recv(1024)  # receive data from the client
    client_socket.sendall(b"+PONG\r\n")  # send the +PONG response
    client_socket.close()  # close the client connection


if __name__ == "__main__":
    main()
