import json
import requests
import sys
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

ipflag = False
ip1 = '172.16.23.197'
ip2 = '172.16.23.97'
gw = '172.16.20.1'
netmask = '255.255.252.0'

def GetNetInfo(sIp):
    url = 'http://{}/GetNetInfo.psp'.format(sIp)
    body = ''
    jsonBody = json.dumps(body)

    #print(jsonBody)

    rep = requests.post(url, data=jsonBody, timeout=3)

    print(rep.text)

def SetNetInfo(sIp, ip, gw, mask):
    url = 'http://{}/SetNetInfo.psp'.format(sIp)
    body = {
        'bakDns':'0.0.0.0',
        'device':0,
        'gateway':gw,
        'ip':ip,
        'ipv6':'::',
        'ipv6Gateway':'::',
        'ipv6PrefixLen':0,
        'mainDns':
        '0.0.0.0',
        'mask':mask,
        'prot':0
    }
    jsonBody = json.dumps(body)

    # print(jsonBody)

    rep = requests.post(url, data=jsonBody, timeout=3)

    print(rep.text)  

def SetDhcpNetInfo(sIp):
    url = 'http://{}/SetNetInfo.psp'.format(sIp)
    body = {
        'bakDns':'0.0.0.0',
        'device':0,
        'gateway':'0.0.0.0',
        'ip':'0.0.0.0',
        'ipv6':'::',
        'ipv6Gateway':'::',
        'ipv6PrefixLen':0,
        'mainDns':
        '0.0.0.0',
        'mask':'0.0.0.0',
        'prot':1
    }
    jsonBody = json.dumps(body)

    # print(jsonBody)

    rep = requests.post(url, data=jsonBody, timeout=3)

    print(rep.text)  

def NetJob():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    global ipflag, ip1, ip2, gw, netmask
    ip = ''
    url = ''
    if ipflag:
        ip = ip1
        url = ip2
    else:
        ip = ip2
        url = ip1
    ipflag = not ipflag

    print('job step 1')
    GetNetInfo(url)
    print('job step 2')
    if ipflag:
        SetNetInfo(url, ip, gw, netmask)
    else:
        SetDhcpNetInfo(url)
    print('job step 3')

if __name__ == '__main__':
    print('arg cnt:{} arg0:{} arg1:{}'.format(len(sys.argv), sys.argv[0], sys.argv[1]))
    index = int(sys.argv[1])

    #global ip1, ip2, gw, netmask
    if index == 1:
        print("index 1")
        ip1 = '172.16.26.217'
        ip2 = '172.16.26.17'
        gw = '172.16.26.1'
        netmask = '255.255.254.0'
    elif index == 2:
        print("index 2")
        ip1 = '172.16.27.173'
        ip2 = '172.16.27.73'        
        gw = '172.16.26.1'
        netmask = '255.255.254.0'

    sched = BlockingScheduler()
    sched.add_job(NetJob, 'interval', seconds=1)
    sched.start()
    
    
    
    



