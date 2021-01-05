# helium-miner-config

This software is a re-write of the gateway-config software provided by Helium for Helium Miners (https://github.com/helium/gateway-config).

The goal is to make a version that is able to run inside a docker container, specifically on Balena due to it not supporting connman.

The re-written version is also planned to use Python instead of Erlang.

# Acknowledgements

* https://github.com/Douglas6/cputemp For the BLE Base code
* https://github.com/helium/gateway-config for the base Helium App.
