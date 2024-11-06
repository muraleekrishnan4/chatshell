# ChatXAI Bot

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
- Gemini API (Optional)

## Usage
1. Register XMPP two accounts - One for server and One for client (mobile).
2. Install XMPP client application on Mobile (Xabber or Conversations).
3. Setup a cloud server (Use Oracle free lifetime Virtual Machine)
4. Download and Install ChatXAI.
5. Install the requirements.
6. Set up your XMPP credentials in `config.py`.
7. Configure Gemini API from https://aistudio.google.com/app/apikey.
8. Set up the tool that needs to be run and set the command to run (without arguments) in `config.py`.
7. Run the bot using `nohup python3 chatxai.py &`.


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
        <img src="https://github.com/user-attachments/assets/5662810e-1783-4e91-89b8-83dd7e64d2c7" alt="Gathering data on a domain" width="300" height="300" />
        <p><em>Executing a command using XMPP using <br>ChatXAI and receiving real-time updates</em></p>
      </td>
      <td align="center">
        <img src="https://github.com/user-attachments/assets/0d5fb703-1b49-4e27-a0c6-2798ce00a6fd" alt="Executing a command" width="300" height="300" />
        <p><em>Output from executing the command from the <br> XMPP client using ChatXAI</em></p>
      </td>
    </tr>
</table>
</kbd>


## Future Work    
+ More Security
+ Use Multiple tools


## License
This project is licensed under the MIT License.
