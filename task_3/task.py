from scapy.all import *

NETWORK = "192.168.88.0/24"
FILE_NAME = "test_mac.txt"
FILE_OUTPUT = "log.txt"


def scan_network(network: str) -> dict:
    """
    arp scan network
    :param network:
    :return: dict mac-address - ip
    """
    ans, unans = arping(network, verbose=0)
    result = {}
    for s, r in ans:
        result[r[Ether].src] = s[ARP].pdst
        print(f"{r[Ether].src} {s[ARP].pdst}")
    return result


def ip_ping(
        scan: dict,
        file_name: str = FILE_NAME,
        file_output: str = FILE_OUTPUT):
    """
    ping ip device
    :param scan: network_map
    :param file_name: file name device - mac address
    :param file_output: log file
    :return:
    """

    with open(file_name, 'r') as file:
        dict_mac_name = {row.split(" - ")[1] : row.split(" - ")[0] for row in file.read().splitlines()}
        with open(file_output, "w") as log:
            for mac, name in dict_mac_name.items():
                if mac in scan:
                    packet = IP(dst=scan[mac], ttl=20) / ICMP()
                    reply = sr1(packet, timeout=2)
                    if not (reply is None):
                        log_text = f"name {name} mac address {mac} - online have ip {scan[mac]}\n"
                    else:
                        log_text = f"name {name} mac address {mac} - online have ip {scan[mac]} Timeout waiting for {packet[IP].dst}\n"
                else:
                    log_text = f"name {name} mac address {mac} - offline have not ip\n"
                print(log_text)
                print(f"log file {file_name}")
                log.write(log_text)


if __name__ == '__main__':
    network_map = scan_network(NETWORK)
    ip_ping(network_map)
