from setuptools import setup
import setuptools

setuptools.setup(
    name='wtrim',
    version='0.0.1',
    description='trimming the margins',
    author='Gakuto Furuya',
    url='https://github.com/gaato/wtrim',
    packages=[''],
    package_dir={'': 'wtrim'},
    python_requires='>=3.7',
    install_requires=open('requirements.txt').read().splitlines(),
)