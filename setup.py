from setuptools import setup, find_packages

setup(
    name="keysStorage",
    version="0.2",
    package=find_packages(),
    include_packages_data=True,
    install_requires=[
        "click", "pycrypto"
    ],
    entry_points="""
        [console_scripts]
        keys=keyStorage.scripts:cli
    """
)