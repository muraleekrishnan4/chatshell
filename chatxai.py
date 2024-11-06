#!/usr/bin/env python3

import slixmpp
import asyncio
import subprocess
import config
from command_runner import run_tool



class XMPPListenerBot(slixmpp.ClientXMPP):
    def __init__(self, jid, password):
        super().__init__(jid, password)

        # Attach the event handler for session start
        self.add_event_handler("session_start", self.start)

        # Attach the event handler for receiving messages
        self.add_event_handler("message", self.message)

    async def start(self, event):
        # Send presence to notify the server that we're available
        self.send_presence()
        await self.get_roster()
        print("Connected to XMPP server and ready to receive messages.")

    def message(self, msg):
        # Extract the command from the message body
        argument = msg['body']
        print(f"Received command: {argument}")
        
        #Run the tool to fetch the data and save it to output variable.
        output=run_tool(argument)
        
        # Print the command output (for server-side logging)
        print(f"Command output: {output}")
        
        # Reply to the sender with the command output
        msg.reply(f"Command output:\n{output}").send()


print(config.JID, config.PASSWORD)
if (len(config.JID)+len(config.PASSWORD)) > 1:
	# Create the bot and connect
	xmpp = XMPPListenerBot(config.JID, config.PASSWORD)

	# Connect to the XMPP server and start listening
	xmpp.connect()

	# Start processing XMPP messages
	xmpp.process(forever=True)
else:
	print("ERROR: Configure the XMPP account on config.py")
