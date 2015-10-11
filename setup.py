from RestfulClient import __version__
from setuptools import setup, find_packages

setup(
	name = "restful-client",
	version = __version__,
	description = "Generic RESTful API Client",
	author = "Jamie Cressey",
	author_email = "jamiecressey89@gmail.com",
	url = "http://github.com/JamieCressey/python-restful-client",
	install_requires = ["requests>=2.2.1", "simplejson>=3.4.0"],
	packages = find_packages(),
	classifiers = [
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Programming Language :: Python",
		"Programming Language :: Python :: 2.5",
		"Programming Language :: Python :: 2.6",
		"Programming Language :: Python :: 2.7",
		"Topic :: Software Development :: Libraries :: Python Modules"
	],
	long_description = """\
	Generic RESTful API Client for Python
""" )
