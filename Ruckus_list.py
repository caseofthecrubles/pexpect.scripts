import pexpect
import time

list_of_hosts = "172.16.219.14","172.16.219.13","172.16.219.10"
username = "xxxx"
password = "xxxx"
command = "get client-info"

for host in list_of_hosts:
    try:
        # Start the SSH connection
        ssh_command = f"ssh {username}@{host}"
        child = pexpect.spawn(ssh_command)

        #Ruckus weird stuff 
        child.sendline('a')
        child.expect('Please login:')
        print(child.before.decode())

        child.sendline(username)

        # Handle the password prompt
        child.expect('password :')
        child.sendline(password)

        # Wait for the custom command prompt
        child.expect('rkscli:')
        
        # Send the command
        child.sendline(command)
        child.expect('rkscli:')
        print(child.before.decode())

        # Disconnect
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
