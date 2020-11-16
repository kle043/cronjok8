from setuptools import setup, find_packages

NAME = "scheduler"

setup(
    name=NAME,
    version="1.0.0",
    description="A worker",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    package_data={
        NAME: ["job-manifest.yaml"],
    },
    install_requires=["requests==2.21.0", "kubernetes==12.0.1", "pyyaml==5.3.1"],
    entry_points={"console_scripts": [f"{NAME} = {NAME}.__main__:main"]},
)
