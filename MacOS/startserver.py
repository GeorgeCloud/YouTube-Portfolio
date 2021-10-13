from os import system, getpid

live_server_port = 9999
live_server_pid = getpid()

# Start live-server
system(f"live-server -p {live_server_port} ../")
print("To kill server type --> Command + C")
