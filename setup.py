from setuptools import setup

setup(
    name="ssh-key",
    version="0.0.1",
    author="Tom Nixon",
    author_email="sshkey@tomn.co.uk",
    url="http://github.com/tomjnixon/ssh-key",
    license='MIT',
    packages=["sshkey"],
    entry_points={
        'console_scripts': [
            'ssh-key=sshkey:main',
        ],
    },
)

