import paramiko
import time
 


def ssh_get_banner(hostname, username, password):
    """
    SSH into a Cisco device and retrieve the current banner.
    """
    try:
        # Create SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the device
        ssh_client.connect(hostname, username=username, password=password, allow_agent=False, look_for_keys=False)

        # Create a shell session
        ssh_shell = ssh_client.invoke_shell()

        # Wait for the prompt
        time.sleep(1)

        # Send command to get banner
        ssh_shell.send("show running-config | include banner\n")

        # Wait for command execution
        time.sleep(2)

        # Read output
        output = ssh_shell.recv(65535).decode('utf-8')

        # Close SSH client
        ssh_client.close()

        # Extract banner
        banner_lines = [line.strip() for line in output.splitlines() if 'banner' in line.lower()]
        if banner_lines:
            return '\n'.join(banner_lines)
        else:
            return "No banner found."

    except Exception as e:
        return f"Error: {e}"

def ssh_execute_command(hostname, username, password, command):
    """
    SSH into a Cisco device and execute a command.
    """
    try:
        # Create SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect to the device
        ssh_client.connect(hostname, username=username, password=password, allow_agent=False, look_for_keys=False)

        # Execute the command
        stdin, stdout, stderr = ssh_client.exec_command(command)

        # Wait for command execution
        time.sleep(2)

        # Read output
        output = stdout.read().decode('utf-8')

        # Close SSH client
        ssh_client.close()

        return output.strip()

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Replace these values with your device's information
    hostname = '204.1.2.5'  
    username = 'admin'  
    password = 'Maglev123'

    # Task 1: Get the current banner
    current_banner = ssh_get_banner(hostname, username, password)
    print("Current banner:")
    print(current_banner)

    # Task 2: Check and execute commands based on the banner
    if current_banner == "Test Banner":
        command_to_execute = "banner motd Test Banner"
        result = ssh_execute_command(hostname, username, password, command_to_execute)
        print("Executed command:", command_to_execute)
        print("Command output:", result)
    elif current_banner == "This Device is part of Solution Automation Testbed Please log off if you are not intended user Contact phannguy for further details":
        command_to_execute = 'banner motd "This Device is part of Solution Automation Testbed Please log off if you are not intended user Contact phannguy for further details"'
        result = ssh_execute_command(hostname, username, password, command_to_execute)
        print("Executed command:", command_to_execute)
        print("Command output:", result)
    else:
        print("No matching banner found or failed to retrieve the banner.")
