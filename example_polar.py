#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
StarryNet: empowering researchers to evaluate futuristic integrated space and terrestrial networks.
author: Zeqi Lai (zeqilai@tsinghua.edu.cn) and Yangtao Deng (dengyt21@mails.tsinghua.edu.cn)
"""

from starrynet.sn_observer import *
from starrynet.sn_orchestrater import *
from starrynet.sn_synchronizer import *

if __name__ == "__main__":
    # Starlink 4*4: 16 satellite nodes, 2 ground stations.
    # The node index sequence is: 16 sattelites, 2 ground stations.
    # In this example, 16 satellites and 2 ground stations are one AS.

    AS = [[1, 18]]  # Node #1 to Node #18 are within the same AS.
    GS_lat_long = [
        [50.110924, 8.682127], [46.635700, 14.311817]
    ]  # latitude and longitude of frankfurt and  Austria
    configuration_file_path = "./config_polar.json"
    hello_interval = 1  # hello_interval(s) in OSPF. 1-200 are supported.

    print('Start StarryNet Polar Example.')
    sn = StarryNet(configuration_file_path, GS_lat_long, hello_interval, AS)
    sn.create_nodes()
    sn.create_links()
    sn.run_routing_deamon()

    time_index = 5

    # No inter-plane ISL connection
    sat1 = 1
    sat5 = 5
    sn.set_ping(sat1, sat5, time_index)

    # Inter-plane ISL connection
    sat2 = 2
    sat6 = 6
    sn.set_ping(sat2, sat6, time_index)

    # Same behavior after link update
    time_index = 15
    sn.set_ping(sat1, sat5, time_index)
    sn.set_ping(sat2, sat6, time_index)

    sn.start_emulation()
    sn.stop_emulation()
