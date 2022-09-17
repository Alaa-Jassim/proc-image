
from setuptools import setup, find_packages

setup(
    name='ProcImage',
    version = "0.0.1",
    author = "Alaa Jassim Mohammed",
    author_email = "alobede2001alobede@gmail.com",
    description = "Small and simple image processing library",
    packages=find_packages(),
    url="https://github.com/Alaa-Jassim/ProcImage",
    long_description=open('README.md').read(),
    install_requires=[
        "Pillow",
        "prettytable",
        ],
    dependency_links = [
     "https://github.com/Alaa-Jassim/ProcImage",
    ],

    include_package_data=True,
)
