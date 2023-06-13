# Citation for the following file
# Date: 04-14-2023
# Adapted from 
# Kurose and Ross, Computer Networking: A Top-Down Approach, 8th Edition,Pearson
# Page 161

from socket import *

def rock_paper_scissors(clientSocket):
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
    
    # Sending and receiving the selection
    clientSocket.send(selection.encode())
    serverSelection = clientSocket.recv(1024).decode()

    # Printing server selection
    print("Your opponent chose: " + serverSelection)

    # Logic to decide who won the game
    if (serverSelection == selection):
        print("It's a tie!")

    elif ((serverSelection == 'rock' and selection == 'scissors')
    or (serverSelection == 'scissors' and selection == 'paper')   
    or (serverSelection == 'paper' and selection == 'rock')
    ):
        print("You lost!")
    
    else:
        print("You won!")

# Defining the address and port to connect
server_port = 4800
server_address = "localhost"

# Creating the socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((server_address, server_port))

print("Connected to: " + server_address + " on port: " + str(server_port))

# Introduction to the application for the user
intro1 = "Type /q to quit.\n"
intro2 = "Enter a message to send. Please wait for the input prompt before entering a message.\n"
intro3 = "Enter 'play rps' to play rock paper scissors."
print(intro1 + intro2 + intro3)

# Loop for communication between sever and client
while True:
    # Input from user
    userIn = input("Enter Input>")
    clientSocket.send(userIn.encode())

    # Quitting the application
    if (userIn == "/q"):
        print("Shutting down!")
        break

    # Starting the rock paper scissors game
    if (userIn == "play rps"):
        rock_paper_scissors(clientSocket)
        
    # Receiving from the server
    fromServer = clientSocket.recv(1024).decode()
    print(fromServer)

    # Quitting application
    if (fromServer == "/q"):
        print("Server has requested shutdown. Shutting down!")
        break

    # Starting rock paper scissors game
    if (fromServer == "play rps"):
        rock_paper_scissors(clientSocket)
        continue

# Closing the socket
clientSocket.close()
