import subprocess
def create_network(name: str):
    result = subprocess.run(["nebula-cert", "ca", "-name", name, "-cert", f"{name}.crt", "-key", f"{name}.key"], capture_output=True, text=True)
    if result.returncode == 0:
        print("Creating network:", name)
        with open("overlaynetworks.log", "a") as f:
            f.write(f"NETWORK {name} \n")
    else:
        print("Error creating network:", name, "\n Error:", result.stderr)

def node(network: str, name: str = "node1", ip_range: str = "10.0.0.0/24"):
    
    result = subprocess.run(["mkdir",f"{name}", "&&","cd ", f"{name}", "&&", "nebula-cert", "sign", "-name", name, "-ip", f"{ip_range}", "-cert", f"{name}.crt", "-key", f"{name}.key", "-ca-cert", f"{network}.crt", "-ca-key", f"{network}.key "], capture_output=True, text=True)
    if result.returncode == 0:
        print("Creating node:", name, "in network:", network)
        with open("overlaynodes.log", "a") as f:
            f.write(f"NODE {name} IN NETWORK {network} \n")
    else:
        print("Error creating node:", name, "\n Error:", result.stderr)