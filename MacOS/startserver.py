from os import system

live_server_port = 9999

# Start live-server
system(f"live-server -p {live_server_port} ../")
print("To kill server type --> Command + C")
