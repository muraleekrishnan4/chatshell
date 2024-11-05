# ChatShell Bot

⭐Open For Contributions⭐

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

<kbd>
<table>
    <tr>
      <td align="center">
        <img src="https://github.com/user-attachments/assets/5ce67568-7520-4de5-aa4a-6a7e7349bb5e" alt="Gathering data on a domain" width="300" height="300" />
        <p><em>Executing a command using XMPP using <br>ChatShell and receiving real-time updates</em></p>
      </td>
      <td align="center">
        <img src="https://github.com/user-attachments/assets/3b1f0d74-17c8-421b-b14e-77d0349ea5e9" alt="Executing a command" width="300" height="300" />
        <p><em>Output from executing the command from the <br> XMPP client using ChatShell</em></p>
      </td>
    </tr>
</table>
</kbd>





## License
This project is licensed under the MIT License.
