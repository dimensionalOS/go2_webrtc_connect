from setuptools import setup, find_packages
import os
import sys
import shutil
import subprocess

# Handle submodule installation
def get_aioice_lib():
    aioice_dir = os.path.join('libs', 'aioice')
    
    # Check if submodule exists
    if not os.path.isdir(aioice_dir) or not os.listdir(aioice_dir):
        print("Initializing submodules...")
        subprocess.check_call(['git', 'submodule', 'update', '--init', '--recursive'])
    
    # Make sure the directory exists after submodule init
    if os.path.isdir(aioice_dir):
        return ['libs.aioice']
    return []

# Find all packages including the submodule
packages = find_packages() + get_aioice_lib()

# Define package data for inclusion in the wheel
package_data = {}
wasm_files = [os.path.join('go2_webrtc_driver', '**', '*.wasm')]

setup(
    name='go2-webrtc-connect',
    version='1.0.0',
    author='legion1581',
    author_email='legion1581@gmail.com',
    packages=packages,
    package_dir={'libs.aioice': 'libs/aioice'},
    package_data={
        '': ['*.wasm'],
        'libs.aioice': ['*.py'],
    },
    include_package_data=True,
    install_requires=[
        'aiortc==1.9.0', 
        'pycryptodome',
        'opencv-python',
        'sounddevice',
        'pyaudio',
        'requests',
        'wasmtime',
        'flask-socketio',
        'lz4',
        'pydub'
    ],
)
