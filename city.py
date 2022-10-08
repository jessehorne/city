"""
City: Become rich, gain power and run the city.

by dock
"""

from pyspades.collision import vector_collision
from pyspades.constants import CTF_MODE

ALWAYS_ENABLED = True
WATER_SPAWNS = False

def apply_script(protocol, connection, config):
    class CityProtocol(protocol):
        pass

    class CityConnection(connection):
        pass

    return CityProtocol, CityConnection