#!/bin/sh
echo "Updating packages ..."
apt update
apt upgrade -y
apt install tree -y
