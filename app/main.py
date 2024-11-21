import socket
import select

def main():
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    server_socket.listen()

    inputs = [server_socket]
    outputs = []

    while inputs:
        readable, writable, exceptional = select.select(inputs, outputs, inputs)

        for s in readable:
            if s is server_socket:
                connection, client_address = s.accept()
                print(f"Connection from {client_address}")
                connection.setblocking(0)
                inputs.append(connection)
            else:
                data = s.recv(1024)
                if data:
                    print(f"Received {data} from {s.getpeername()}")
                    s.sendall(b"+PONG\r\n")
                else:
                    print(f"Closing connection to {s.getpeername()}")
                    inputs.remove(s)
                    s.close()

        for s in exceptional:
            print(f"Handling exceptional condition for {s.getpeername()}")
            inputs.remove(s)
            s.close()

if __name__ == "__main__":
    main()