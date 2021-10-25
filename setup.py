"""The setup script."""
from setuptools import find_packages
from setuptools import setup

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

requirements = ['Faker',
                'randominfo',
                'dict2xml',
                'json2xml',
                'xmltodict',
                'phone-gen']

setup(
    name='dthok',
    version='1.0.0',
    description="Bulk Test Data Generator",
    author="Palo IT Singapore",
    author_email='SG-PyPi-Group@sg.palo-it.com',
    url='https://github.com/paloitsingapore/dthok',
    install_requires=requirements,

    packages=find_packages(),
    python_requires='>=3.6',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    entry_points={
        'console_scripts': [
            'dthok=src.cli:main',
        ],
    },
    license="MIT license",
    include_package_data=True,
    keywords='dthok',
    zip_safe=False,
    long_description=long_description,
    long_description_content_type="text/markdown",
)