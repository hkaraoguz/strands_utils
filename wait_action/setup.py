

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['wait_action'],
    scripts=['scripts/wait_node.py', 'scripts/wait_node_client.py'],
)

setup(**d)
