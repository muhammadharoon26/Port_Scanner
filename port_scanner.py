#!/bin/python3
import sys
import socket
from datetime import datetime


def get_target():
    if len(sys.argv) == 2:
        try:
            return socket.gethostbyname(sys.argv[1])
        except socket.gaierror:
            print("Hostname could not be resolved")
            sys.exit()
    else:
        print("Invalid amount of arguments")
        print("python3 port_scanner.py <ip>")
        sys.exit()


def scan_port(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        s.close()
    except socket.error:
        print(f"Could not connect to port {port}")


def main():
    target = get_target()
    print("-" * 50)
    print(f"Scanning target {target}")
    print(f"Time started: {datetime.now()}")
    print("-" * 50)
    try:
        for port in range(50, 86):
            print(
                f"Checking port {port}........................................................"
            )
            scan_port(target, port)
    except KeyboardInterrupt:
        print("-" * 50)
        print("Exiting program" + "." * 50)
        print("-" * 50)
        sys.exit()


if __name__ == "__main__":
    main()
