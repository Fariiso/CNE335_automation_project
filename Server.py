import os

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
       """
       Initialize the Server object with the given server IP address.
        Parameters: # public ip address ()
        server_ip (str):  The IP address of the server.
        """
       self.server_ip = server_ip

    def ping(self):
        """
        Ping the server to check if it is reachable.
        Returns:
        bool: True if the server is reachable, False otherwise.
        """
        # Use the appropriate ping command based on the OS
        param = '-n 1' if os.name == 'nt' else '-c 1'
        response = os.system(f"ping {param} {self.server_ip}")
        return response == 0

# User input section
server = Server("ec2-35-93-33-235.us-west-2.compute.amazonaws.com")
if server.ping():
    print(f"{server.server_ip} is reachable")
else:
    print(f"{server.server_ip} is not reachable")