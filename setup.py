from setuptools import setup, find_packages

setup(
    name='pyrva',
    version='0.0.1',
    packages=find_packages(exclude=['tests']),
    install_requires=['numpy'],  # external libraries
    tests_require=['pytest'],  # libraries required for testing
)
