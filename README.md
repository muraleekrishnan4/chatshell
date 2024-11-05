# ChatShell Bot

This project is a Python-based XMPP bot that allows users to execute commands on a remote server via XMPP messages.

## Features
- Execute commands remotely
- Receive real-time updates about command execution
- Safe handling of sensitive information

## Requirements
- Python 3.x
- Slixmpp library
- XMPP account

## Usage
1. Register XMPP two accounts - One for server and One for client (mobile).
2. Install XMPP client application on Mobile (Xabber or Conversations).
3. Setup a cloud server (Use Oracle free lifetime Virtual Machine)
4. Download and Install ChatShell.
5. Install the requirements.
6. Set up your XMPP credentials in `config.py`.
7. Set up the tool that needs to be run and set the command to run (without arguments) in 'config.py'.
7. Run the bot using `nohup python3 chatshell.py &`.


## License
This project is licensed under the MIT License.
