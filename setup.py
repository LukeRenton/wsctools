from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='wsctools',
    version='1.0.1',
    author='Luke Renton',
    description='A collection of helper functions for web scraping',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/LukeRenton/wsctools',
    packages=['wsctools'],
    install_requires=[
        'googletrans==4.0.0-rc1',
        'langdetect==1.0.9',
        'tldextract==5.1.1',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

)