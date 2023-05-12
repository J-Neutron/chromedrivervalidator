from setuptools import setup, find_packages

setup(
    name='chromedriverhandlar',
    version='0.1',
    description='A simple Python library that check, update or download chrome driver',
    author='Joshi Hrithik V',
    author_email='hrithikjoshi987@gmail.com',
    license="BSD",
    url='',
    packages=find_packages(),
    install_requires=['requests==2.28.1',]
)