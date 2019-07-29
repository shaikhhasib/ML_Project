# setup for BDS
#from setuptools import setup, find_packages

setup(
	name='Data_Analysis',
	version='0.0.1',
	url='www.github.com/MuhammadHasib/ML_Project',
	license='BSD',
	author='Muhammad Hasib',
	packages=find_packages(),
	install_requires=['PyQt5','pandas','sqlalchemy','nltk','numpy','jupyter','python-twitter', 'tweepy'],
	entry_points={},
	extras_require={'dev': ['flake8',]},
	)
