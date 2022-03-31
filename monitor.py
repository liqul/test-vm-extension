#!/usr/bin/python

import json
import socket
import urllib.request
import datetime 

metadata_url = "http://169.254.169.254/metadata/scheduledevents?api-version=2020-07-01"
this_host = socket.gethostname()
print("host name:", this_host)


def get_scheduled_events():
    headers = {"Metadata":"true"}
    req = urllib.request.Request(url = metadata_url, headers=headers)
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read())
    return data


def handle_scheduled_events(data):
    for evt in data['Events']:
        eventid = evt['EventId']
        status = evt['EventStatus']
        resources = evt['Resources']
        eventtype = evt['EventType']
        resourcetype = evt['ResourceType']
        notbefore = evt['NotBefore'].replace(" ", "_")
        description = evt['Description']
        eventSource = evt['EventSource']
        if this_host in resources:
            print("+ Scheduled Event. This host " + this_host +
                " is scheduled for " + eventtype +
                " by " + eventSource +
                " with description " + description +
                " not before " + notbefore)
            print("send msg to mq!!!!")


def main():
    data = get_scheduled_events()
    print(datetime.datetime.now(), data)
    handle_scheduled_events(data)


if __name__ == '__main__':
    main()
