from setuptools import setup, find_packages

NAME = 'worker'

setup(
    name=NAME,
    version='1.0.0',
    description='A worker',
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    install_requires=['requests==2.21.0'],
    entry_points={
        "console_scripts": [
            f"{NAME} = {NAME}.__main__:main"
        ]
    },

)