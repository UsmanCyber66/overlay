import subprocess
def network(name: str):
    result = subprocess.run(["mkdir",f"{name}","cd", f"{name}", "nebula-cert", "ca", "-name", name], capture_output=True, text=True)
    if result.returncode == 0:
        print("Creating network:", name)
        subprocess.run(["echo", f"Network {name}:", ">>", f"{name}/filename.txt"])
    else:
        print("Error creating network:", name, "Error:", result.stderr)

def node(name: str, network: str, ip_range: str = "10.0.0.0/24"):
    ip_range=input("Enter the IP range for the node (e.g., 192.168.1.0/24): ")
    result = subprocess.run(["mkdir",f"{name}","cd", f"{name}", "nebula-cert", "sign", "-name", name, "-ip", f"{network}.1.1"], capture_output=True, text=True)
    if result.returncode == 0:
        print("Creating node:", name, "in network:", network)
        subprocess.run(["echo", f"Node {name} in network {network}", ">>", f"{name}/filename.txt"])
    else:
        print("Error creating node:", name, "Error:", result.stderr)