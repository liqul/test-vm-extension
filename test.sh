#!/bin/sh
echo "Updating packages ..."
apt update
apt upgrade -y

# setup a cron job
crontab -l > cron_bkp
echo "0 10 * * * sh /home/test.sh >/dev/null 2>&1" >> cron_bkp
crontab cron_bkp
rm cron_bkp
