from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='foo',
   version='1.0',
   description='Changes text to make it more annoying to read, incoherent, or strange',
   license="MIT",
   long_description=long_description,
   author='St0nkyCheeseMan',
   url="https://github.com/St0nkyCheeseMan/text-seasoning",
)