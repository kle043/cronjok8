from setuptools import setup, find_packages

NAME = 'job_server'

setup(
    name=NAME,
    version='1.0.0',
    description='Some server',
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    install_requires=['uvicorn==0.12.2', 'fastapi==0.61.2', 'prometheus-fastapi-instrumentator==5.5.1'],
    entry_points={
        "console_scripts": [
            f"{NAME} = {NAME}.__main__:main"
        ]
    },

)