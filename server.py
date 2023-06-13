# Citation for the following file
# Date: 06-08-2023
# Adapted from Kurose and Ross, Computer Networking: A Top-Down Approach, 8th Edition,Pearson
# Page 163

from socket import *

def rock_paper_scissors(connectionSocket):
    # Introduction to the game
    print("Welcome to rock paper scissors!")
    options = ['rock', 'paper', 'scissors']
    valid = False

    # Getting the user input and making sure it's valid
    while valid == False:
        selection = input("Choose your selection ('rock', 'paper', or 'scissors'): ")
        if selection in options:
            valid = True
        else:
            print("Invalid selection. Try again!")

    # Sending and receiving selections
    clientSelection = connectionSocket.recv(1024).decode()
    connectionSocket.send(selection.encode())

    # Printing clietn selection
    print("Your opponent chose: " + clientSelection)

    # Logic for determining who won the game
    if (clientSelection == selection):
        print("It's a tie!")

    elif ((clientSelection == 'rock' and selection == 'scissors')
    or (clientSelection == 'scissors' and selection == 'paper')   
    or (clientSelection == 'paper' and selection == 'rock')
    ):
        print("You lost!")
    
    else:
        print("You won!")

# Defining port and address to connect to
server_port = 4800
server_address = "localhost"

# Creating, binding, and listening on a serverSocket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("localhost", server_port))
serverSocket.listen(1)

# Printing connection information
print("Server listening on: " + server_address + " on port: "+ str(server_port))

# Accepting the request
connectionSocket, addr = serverSocket.accept()
client_addr = connectionSocket.getpeername()
client_ip = client_addr[0]
client_port = client_addr[1]
print("Connected by ('" + client_ip + "', " + str(client_port) + ")")

# Waiting for and printing the message from the client
print("Waiting for message...")
fromClient = connectionSocket.recv(1024)
print(fromClient.decode())

# Introduction to the application for the user
intro1 = "Type /q to quit.\n"
intro2 = "Enter a message to send. Please wait for the input prompt before entering a message.\n"
intro3 = "Enter 'play rps' to play rock paper scissors."
print(intro1 + intro2 + intro3)

while True:
    # Getting user input and sending it to client
    userIn = input("Enter Input>")
    connectionSocket.send(userIn.encode())

    # Quitting the application
    if (userIn == "/q"):
        print("Shutting down!")
        break

    # Starting the rock paper scissors game
    if (userIn == "play rps"):
        rock_paper_scissors(connectionSocket)
    
    # Receiving the message from the client and printing it
    fromClient = connectionSocket.recv(1024).decode()
    print(fromClient)

    # Quitting the application
    if (fromClient == "/q"):
        print("Client has requested shutdown. Shutting down!")
        break

    # Starting the rock paper scissors game
    if (fromClient == "play rps"):
        rock_paper_scissors(connectionSocket)
        continue

# Closing the connection socket
connectionSocket.close()
