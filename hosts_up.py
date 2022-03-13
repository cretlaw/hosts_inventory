import os
import nmap
import click


cwd = os.getcwd()
file_name = cwd + "/inv"

@click.command()
@click.option('--hosts','hosts',required=True,help='Can be single IP or subnet.')
def hostsUp(hosts):
    '''
    The script will determine if hosts is up or not and build a inv file that ansible uses in order to get attributes about the host.
    You can pass in a single ip or subnet for example 10.10.162.12 or 10.10.162.0/24
    '''
    scanner = nmap.PortScanner()
    scanner.scan(hosts=hosts, arguments='-n -PE -PA22,443,80,3389')
    hosts_list = [x for x in scanner.all_hosts() if scanner[x].state()
                  == 'up' and scanner[x].has_tcp(22) and not scanner[x].has_tcp(3389)]

    with open(file_name, "w") as inv:
        inv.writelines("[targets]\n")
        for ip in hosts_list:
            inv.writelines(str(ip) + "\n")



if __name__ == '__main__':
    hostsUp()