# hosts_inventory

A simple and easy way to build dynamic inventory list of internal assets.
The internal assets and information gets saved get saved to a file in this directory named `hosts_info.csv` which includes the following info for each asset.

- IP
- Hostname
- Operating System
- Processor(s)
- Core(s)
- Memory(mb)

## Run and Install

1. Must have ansible installed and have ssh access to all assets being queried.
2. Install python dependencies `pip install -r requirements.txt`
3. To run ` python hosts_up.py --hosts <ip or subnet> && ansible-playbook gather_info.yml -i inv -u <ssh username>`


Author: Walter Carbajal
