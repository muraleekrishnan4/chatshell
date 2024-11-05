# command_runner.py

import subprocess
import config

# Define the path to your tool
tool_path = config.TOOL_COMMAND

def run_tool(argument):
    """Runs the specified tool with the provided argument and returns the output."""
    try:
        command = f"{tool_path} {argument}"
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.output}"

