#!/bin/bash
set -e

# Ensure running as root
if [ "$EUID" -ne 0 ]; then
  echo "Run this script as root or with sudo."
  echo "Example: sudo $0"
  exit 1
fi
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo gpg --dearmor -o /usr/share/keyrings/yarn-archive-keyring.gpg 
echo "deb [signed-by=/usr/share/keyrings/yarn-archive-keyring.gpg] https://dl.yarnpkg.com/debian stable main" | sudo tee /etc/apt/sources.list.d/yarn.list 
apt update -y
apt install -y curl python3 python3-pip

ARCH=$(dpkg --print-architecture)

# Get latest release .deb URL
# Download latest release tarball
curl -LO https://github.com/slackhq/nebula/releases/latest/download/nebula-linux-amd64.tar.gz

# Extract and move binary
tar xzf nebula-linux-amd64.tar.gz
sudo mv nebula /usr/local/bin/

echo "All dependencies installed successfully."