from setuptools import setup

from pathlib import Path
from distutils.core import setup
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='topsis_gurleen_102003138',
    packages=['topsis_gurleen_102003138'],
    version='0.3',
    license='MIT',
    description='This package is implementation of Multiple-criteria decision making using Topsis Algorithm',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Gurleen Kaur',
    author_email='gurleen2113@gmail.com',
    url='https://github.com/Gurleen21',
    download_url='https://github.com/Gurleen21/Topsis_Gurleen_102003138.git',
    keywords=['TOPSIS', 'MULTIPLE CRITERIA DECISION MAKING',
              'MCDM'],
    install_requires=[
        'pandas',
        'math',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',

    ],
)
