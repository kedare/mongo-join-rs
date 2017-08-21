
from setuptools import setup

setup(
    name="mongo-join-rs",
    version="0.1",
    description="Small utility to join/leave MongoDB replicaset",
    author="kedare",
    author_email="mathieu.poussin@netyxia.net",
    url="https://blog.kedare.net/",
    classifiers = [
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5"
    ],
    packages=[
        "mongo_join_rs"
    ],
    install_requires=[
        "pymongo==3.4.0",
        "logbook==1.0.0"
    ],
    entry_points= {
        "console_scripts": [
            "mongo_join_rs = mongo_join_rs.application:main"
        ]
    }
)
