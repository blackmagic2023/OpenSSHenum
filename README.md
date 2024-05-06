# SSH User Enumeration Tool

This tool is designed to enumerate valid usernames on an SSH service by exploiting a vulnerability in the SSH protocol. It's important to note that this tool should only be used for ethical purposes with proper authorization.

## Features

- Enumerates valid usernames on an SSH service.
- Exploits a vulnerability in the SSH protocol to achieve enumeration.
- Supports customization and modification for different use cases.
- Includes error handling and logging for improved reliability.

## How It Works

The tool works by sending specially crafted packets to the SSH service. It exploits a vulnerability in the SSH protocol to determine whether a username is valid or not.

## Prerequisites

- Python 3 installed on your system.
- Permission to interact with SSH services.

## Usage

1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using Python 3 with the following command:

    ```bash
    python3 ssh_user_enum.py <target_ip> -p <port> <username>
    ```

    Replace `<target_ip>` with the IP address of the target SSH service.
    Replace `<port>` with the port number of the SSH service (optional, default is 22).
    Replace `<username>` with the username you want to check for validity.

## Modifying the Code

The code can be modified to suit different use cases. Here are some possible modifications:

- Customizing the payload sent to the SSH service.
- Adding additional error handling or logging.
- Integrating with other tools or scripts.

## Example Payloads

### Custom Payload 1

Payload:
```python
def custom_payload(*args, **kwargs):
    pass

paramiko.auth_handler.AuthHandler._client_handler_table[paramiko.common.MSG_USERAUTH_FAILURE] = custom_payload
```

### Custom Payload 2

Description: This payload is optimized for targeting SSH services with custom authentication mechanisms.
```python
def custom_payload(*args, **kwargs):
    pass

paramiko.auth_handler.AuthHandler._client_handler_table[paramiko.common.MSG_SERVICE_ACCEPT] = custom_payload
```

## Example

To enumerate valid usernames on an SSH service running on `192.168.1.100` with the default port (22) and checking the username `admin`, run the following command:

```bash
python3 ssh_user_enum.py 192.168.1.100 admin
```

## Disclaimer

This tool is provided for educational and ethical purposes only. Misuse of this tool may violate laws and regulations. Use it responsibly and with proper authorization.
