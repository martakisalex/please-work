from setuptools import setup, find_packages

setup(
    name="python-sample",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "python-sample=main:main",
        ],
    },
)
