from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

description = "The magic_patch is a simple library that provides " \
              "the ability to patch an object in different scopes at once. " \
              "Now you can patch objects easily like magic."

setup(
    name='magic_patch',
    version='0.0.1',
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/dart-neitro/magic_patch',
    author='Konstantin Neitro',
    author_email='neitro88@gmail.com',
    packages=find_packages(include=['magic_patch']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
