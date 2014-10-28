from setuptools import setup, find_packages

setup(
    name='PyRegistrar',
    version='1.0.0',
    author='Gorbin',
    author_email='gorbinphilip@gmail.com',
    packages=find_packages(exclude=[]),
    scripts=['register'],
    url='https://github.com/gorbinphilip/PyRegistrar',
    description='A console based application that accepts details of any configured object and exports those data in different file formats.',
    long_description=open('README.md').read(),
    install_requires=[
        "argparse==1.2.1",
	"reportlab==3.0",
       ],
)
