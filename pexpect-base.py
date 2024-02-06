import pexpect
import time

# SSH credentials and details
host = "your_host"
username = "your_username"
password = "your_password"
command = "xxxxxxxxxxxxx"

while True:
    try:
        # Start the SSH connection
        ssh_command = f"ssh {username}@{host}"
        child = pexpect.spawn(ssh_command)

        # Handle the password prompt
        child.expect('password:')
        child.sendline(password)

        # Wait for the custom command prompt
        child.expect('#')
        
        # Send the command
        child.sendline(command)

        child.expect('#')
        print(child.before.decode())

        child.sendline('exit')
        child.expect(pexpect.EOF)

    except pexpect.exceptions.EOF:
        print("SSH session failed or was unexpectedly closed")
    except pexpect.exceptions.TIMEOUT:
        print("SSH session timed out")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Wait for 60 seconds
    time.sleep(60)
