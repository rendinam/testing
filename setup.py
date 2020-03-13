from setuptools import setup, find_packages

pkgname='testertron'

setup(
    name=pkgname,
    version='0.0.1',
    use_scm_version={'write_to': f'{pkgname}/version.py'},
    setup_requires=['setuptools_scm'],
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
