# DTRC

Distributed Ticket Reservation System

### Group 9 Distributed System term project at IITKGP Spring-2020

### How to Run

Note: The project requires python3 (for the backend) and NodeJS (for the client)

1. clone repository and create a new virtual environment using `python -m venv venv`
2. install dependencies using 'pip install -r requirements.txt'
3. In `client/` directory, install dependencies using 'npm install`
4. To run the client, in `client/` directory open a new terminal and run `npm start` . This opens the browser and start the client on `localhost:3000`
5. To run the reverseproxy, in the `reverseproxy` directory, run `python main.py`
6. Open three new terminals in `server` directory and do as follows:
    1. In first terminal, `python main.py`
    2. In second terminal, `python main.py 8002`
    3. In third terminal, `python main.py 8003`

Make sure that the port numbers are correct. Otherwise, a `bind()` error will be thrown.  
Each of the server replicas will create a sqlite database with its port number as its name.  
If a .db file with its port no. already exists, then it won't be recreated.  
To reset the database simply delete the .db files from the `server` directory.
