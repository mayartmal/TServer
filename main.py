import socket
from http.client import responses


def start_my_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("127.0.0.1", 2000)) #>1024 port
        server.listen(4)
        while True:
            print("Working...")
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode('utf-8')
            content = load_page_from_get_requests(data)
            client_socket.send(content)
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print("Shut down the socket")



def load_page_from_get_requests(request_data):
    HDRS = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n"
    path = request_data.split(" ")[1]
    response = ''
    with open('views'+path, 'rb') as file:
        response = file.read()
    return HDRS.encode('utf-8') + response

if __name__ == "__main__":
    start_my_server()