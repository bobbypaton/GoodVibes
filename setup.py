from setuptools import setup
import io

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name='goodvibes',
  packages=['goodvibes'],
  version='4.0',
  description='A python program to compute corrections to thermochemical data from frequency calculations',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='Paton Research Group',
  author_email='patonlab@colostate.edu',
  url='https://github.com/patonlab/goodvibes',
  download_url='https://github.com/patonlab/GoodVibes/archive/v4.0.zip',
  keywords=['compchem', 'thermochemistry', 'gaussian', 'vibrational-entropies', 'temperature'],
  classifiers=[],
  install_requires=['numpy', 'pymsym', 'cclib', 'numpy', 'rdkit'],
  python_requires='>=3.7',
  include_package_data=True,
  entry_points={
    'console_scripts': [
        'goodvibes = goodvibes.GoodVibes:main',
    ],
  }
)
