"""Go2 WebRTC driver package for connection to Unitree Go2 robot."""

import sys
import os
import importlib.util

# handles both development mode and wheel installation
try:
    from libs.aioice import *
except ImportError:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    libs_path = os.path.abspath(os.path.join(current_dir, '..', 'libs'))
    aioice_path = os.path.join(libs_path, 'aioice', 'src')
    if os.path.exists(aioice_path):
        sys.path.insert(0, aioice_path)