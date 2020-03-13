from setuptools import setup, find_packages

setup(
    name='testertron',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'testertron = testertron.cli.main:main',
        ],
    },
    #install_requires=[
    #    'github3.py'
    #],
    extras_require={
        'test': [
            'pytest',
        ],
    }
)
