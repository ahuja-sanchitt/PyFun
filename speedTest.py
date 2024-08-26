'''
This is a simple program for doing a speedtest using python.
Library used: speedtest

'''

import speedtest as st


def testSpeed():
    test=st.Speedtest()

    servers =test.get_servers()
    print(f"Servers are: {servers}")

    
    down_speed=test.download()
    down_speed=round(down_speed/10**6,2) #To Convert speed into Mbp/s
    print(f"Download Speed is: {down_speed} Mbps")

    up_speed=test.upload()
    up_speed=round(up_speed/10**6,2) #To Convert speed into Mbp/s
    print(f"Upload Speed is: {up_speed} Mbps")

    ping=test.results.ping
    print(f"Ping: {ping}")    


if __name__=="__main__":
    testSpeed()    


