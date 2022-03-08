"""
Configuration required for setup.py.
"""
from setuptools import find_packages, setup

setup(
    name='DjangoListMaker',
    version='1.0.0',
    description='Project takes text, returns list of translations',
    author='Katarzyna Witkowska',
    author_email='k.witkowska008@gmail.com',
    url='https://github.com/witkka/DjangoListMaker',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django',
        'django-widget-tweaks',
        'beautifulsoup4',
        'requests',
        'asyncio',
        'flake8',
    ],
    setup_requires=['pytest-runner', 'black'],
    tests_require=['pytest'],
    scripts=['manage.py'],
)
