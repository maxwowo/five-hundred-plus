from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="fivehundredplus",
    version='0.0.1',
    description='Quickest way to reach 500+ connections on LinkedIn',
    long_description=long_description,
    author='Max Wo',
    author_email='maxwo@protonmail.com',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.5, <4'
)
