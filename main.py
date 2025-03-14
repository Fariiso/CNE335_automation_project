# This is the template code for the CNE335 Final Project
# Abdo Mohamed
# CNE 335 Winter

import os
import subprocess
#import pdb

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, hostname):
        """
        Initialize the Server object with the given hostname.
        Parameters:
        hostname (str): The hostname of the server.
        """
        self.hostname = hostname
        print(f"Initialized Server with hostname: {self.hostname}")  # Debugging print statement

    def ping(self):
        """
        Ping the server to check if it is reachable.
        Returns:
        tuple: (bool, str) A tuple containing a boolean indicating if the server is reachable,
        and the output message from the ping command.
        """

        # Set a breakpoint for debugging
        # pdb.set_trace()

        # Use the appropriate ping command based on the OS
        param = '-n 5' if os.name == 'nt' else '-c 5'  # Adjusted to 4 pings for more output
        command = f"ping {param} {self.hostname}"
        print(f"Pinging {self.hostname} with command: {command}")  # Debugging print statement

        # Execute the ping command and capture the output
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Capture the full output for multiple "Reply from" lines
        full_output = result.stdout

        print(f"Ping response: {result.stdout}")  # Debugging print statement
        return (result.returncode == 0, result.stdout)


def print_program_info():
    #Name changed to Abdo Mohamed
    print("Server Automator v0.1 by Abdo Mohamed")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # Created a Server object
    hostname = "ec2-35-93-33-235.us-west-2.compute.amazonaws.com"
    server = Server(hostname)

    # Call the ping method once and store the result
    ping_result, ping_output = server.ping()

    # Use the stored result for further checks and prints
    print(f"Ping result: {ping_result}")  # Debugging print statement
    if ping_result:
        print(f"{server.hostname} is reachable")
    else:
        print(f"{server.hostname} is not reachable")

        # Print the stored result and ping output
    print(f"Final ping result: {ping_result}")
    print(f"Ping output:\n{ping_output}")