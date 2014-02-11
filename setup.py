#!/usr/bin/env python
from setuptools import setup, Command
import subprocess


class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        errno = subprocess.call(['py.test'])
        raise SystemExit(errno)

setup(
    name='FancyText',
    version='0.2',
    description='Fancy up that terminal text.',
    license='Apache',
    url='https://github.com/freejoe76/fancytext',
    author='Joe Murphy',
    author_email='joe.murphy@gmail.com',
    packages=['fancytext'],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    )
