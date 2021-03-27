from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='StockScrap',
    version='0.1',
    description='Stock data scrapper using Python for financial data and technical data. Data is downloaded from MarketWatch.com and Yahoo Finance.',
    long_description=open('README.md').read(),
    url='https://github.com/rawsashimi1604/StockScrap',
    author='Gavin Loo',
    author_email='looweiren@gmail.com',
    license='MIT',
    classifiers=classifiers,
    packages=find_packages(),
    install_requires = [
        'pandas', 
        'numpy', 
        'bs4', 
        'requests',
        'pandas_market_calendars',
        'pprint',
        'yfinance',
        'PyQt5'
    ]
)