from setuptools import setup

setup(
    name='wsctools',
    version='0.1.2',
    packages=['wsctools'],
     install_requires=[
        'googletrans==4.0.0-rc1',
        'langdetect==1.0.9',
        'tldextract==5.1.1',
    ],
)