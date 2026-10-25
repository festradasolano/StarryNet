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
        [70.322521, -149.871954], [78.229742, 15.407738]
    ]  # latitude and longitude of Kuparuk (USA) and Svalbard (Norway)
    configuration_file_path = "./config_polar_long.json"
    hello_interval = 1  # hello_interval(s) in OSPF. 1-200 are supported.

    print('Start StarryNet Polar Example.')
    sn = StarryNet(configuration_file_path, GS_lat_long, hello_interval, AS)
    sn.create_nodes()
    sn.create_links()
    sn.run_routing_deamon()

    # Case 1: no initial inter-orbit ISL sats; connect at 470s
    sats_case1 = [1, 5]
    sn.set_ping(sats_case1[0], sats_case1[1], 230)  # disconnected
    sn.set_ping(sats_case1[0], sats_case1[1], 465)  # disconnected
    sn.set_ping(sats_case1[0], sats_case1[1], 470)  # connecting
    sn.set_ping(sats_case1[0], sats_case1[1], 475)  # connected

    # Case 2: initial inter-orbit ISL sats; disconnect at 230s
    sats_case2 = [2, 14]
    sn.set_ping(sats_case2[0], sats_case2[1], 225)  # connected
    sn.set_ping(sats_case2[0], sats_case2[1], 230)  # disconnecting
    sn.set_ping(sats_case2[0], sats_case2[1], 235)  # disconnected
    sn.set_ping(sats_case2[0], sats_case2[1], 470)  # disconnected

    # Case 3: inter-orbit ISL sats during 480s
    sats_case3 = [2, 6]
    sn.set_ping(sats_case3[0], sats_case3[1], 230)  # connected
    sn.set_ping(sats_case3[0], sats_case3[1], 470)  # connected

    sn.start_emulation()
    sn.stop_emulation()