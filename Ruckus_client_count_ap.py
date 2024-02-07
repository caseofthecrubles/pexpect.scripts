import pexpect
import time
import sys

list_of_hosts = "1.1.1.1","2.2.2.2","3.3.3.3"
username = "xxxxxxxxx"
password = "xxxxxxxxxx"
command = "get client-info"
globalcc = 0

for host in list_of_hosts:
    try:
        # Start the SSH connection
        ssh_command = f"ssh -oStrictHostKeyChecking=no -oKexAlgorithms=+ecdh-sha2-nistp256 {username}@{host}"
        child = pexpect.spawn(ssh_command)

        child.expect('login:')
        #print(child.before.decode())

        child.sendline(username)

        child.expect('password :')
        child.sendline(password)

        child.expect('rkscli:')

        child.sendline(command)
        child.expect('rkscli:')
        before_decode = (child.before.decode())
        beforestr = str(before_decode)

        lines = beforestr.splitlines()
        count = (lines[2])

        countsplt = count.split(" ")
        client_count = (countsplt[2])
        globalcc += int(client_count)
        #print(str(before_out))
        
        # Disconnect
        child.sendline('exit')
        child.expect(pexpect.EOF)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

print(globalcc)
