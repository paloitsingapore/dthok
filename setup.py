"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['Faker==8.8.2',
                'Pillow==8.2.0',
                'dict2xml==1.7.0',
                'json2xml==3.6.0',
                'xmltodict==0.11.0']

test_requirements = [ ]

setup(
    author="Bishnu Prasad Panda",
    author_email='bppanda@sg.palo-it.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Bulk Test Data Generation",
    entry_points={
        'console_scripts': [
            'raftnode=raftnode.cli:main',
        ],
    },
    install_requires=requirements,
    extras_require={
        'rocksdb': ['rocksdb==0.7.0'],
    },
    license="MIT license",
    #long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='raftnode',
    name='raftnode',
    packages=find_packages(include=['raftnode', 'raftnode.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/paloitsingapore/D-thok',
    version='0.1.1',
    zip_safe=False,
)