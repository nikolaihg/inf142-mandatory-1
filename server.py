from socket import *
import json

# "database"
database = {
    100 : {
    "tittel": "Hva skal jeg ha til middag?",
    "alternativ": {
        "Pølse": 0, "Hamburger": 0, "PIzza": 0
        }
    }  
}

def show_votes(problemID):
    return f"vis stemmer() {problemID}"

def show_problems():
    return "vis problemer()"

def show_problem(problemID):
    return f"vis problem() {problemID}"

def handle_client_input(choice):
    if choice == "2":
        return ""
    elif choice.startswith("3"):
        parts = choice.split()
        if len(parts) == 3:
            problem_id = int(parts[2])
            return show_problem(problem_id)
        else:
            return "Invalid request format."
    else:
        return "Unknown command."

def start_server(serverPort):
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", serverPort))
    serverSocket.listen(1)
    print("Server has started!")

    try:
        while True:
            connectionSocket, addr = serverSocket.accept()
            print(f"Connected to {addr}")
            try:
                while True:
                    message = connectionSocket.recv(1024).decode()
                    if not message or message.lower() == "exit":
                        break

                    print(f"From client: {message}")
                    response = handle_client_input(message)
                    connectionSocket.send(response.encode())

            except Exception as e:
                print(f"Error: {e}")
            finally:
                connectionSocket.close()
                print("Connection socket closed")
    except KeyboardInterrupt:
        print("\nServer is shutting down...")
    finally:
        serverSocket.close()
        print("Server socket closed.")

def close_server(serverSocket):
    serverSocket.close()
    print("Server socket closed.")

start_server(3000)