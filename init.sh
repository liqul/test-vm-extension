#!/bin/sh
echo "Updating packages ..."
apt update
apt upgrade -y

# download the monitor script
mkdir /monitor
cd /monitor
wget https://raw.githubusercontent.com/liqul/test-vm-extension/main/monitor.py --directory-prefix=/monitor/

# setup a cron job
crontab -l > cron_bkp
echo "* * * * * /usr/bin/python3 /monitor/monitor.py >> /monitor/mon.log 2>&1" >> cron_bkp
crontab cron_bkp
rm cron_bkp
