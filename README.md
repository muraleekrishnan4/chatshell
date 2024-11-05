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


## Sample Use Cases
- OSINT Data Gathering
- Can be used in Reconnaissance for Penetration Testing or Bug Bounty Hunting
- Executing Automated Tasks
- Remote System Monitoring

## Screenshots
![image](https://github.com/user-attachments/assets/9ac57b2f-8608-4834-820a-8d82efc21166)
Example of gathering data on a domain on XMPP Client using ChatShell and receiving real-time updates.

![image](https://github.com/user-attachments/assets/1f3ca3ca-7a07-45a4-9322-388b85c18991)
Example of running Spiderfoot to gather data.

## License
This project is licensed under the MIT License.
