
import socket

target = input("Enter target IP: ")
port = int(input("Enter port number: "))

print("\nScanning target:", target)
print("Scanning port:", port)
print("-" * 35)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
result = s.connect_ex((target, port))

if result == 0:
    print("[+] Port", port, "is OPEN")
else:
    print("[-] Port", port, "is CLOSED or FILTERED")

s.close()

print("Scanning completed!")
