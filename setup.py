from os.path import dirname, join

from setuptools import setup, find_packages



version = '0.0.1'

setup(
    name = 'cmsplugin-button',
    version = version,
    description = "Django CMS Plugin for a Button",
    long_description = open(join(dirname(__file__), 'README')).read() + "\n" + 
                       open(join(dirname(__file__), 'HISTORY')).read(),
    classifiers = [
        "Framework :: Django",
        "Development Status :: 4 - Beta",
        #"Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License"],
    keywords = 'django cms plugin button',
    author = 'Texas A&M University, College of Architecture',
    author_email = 'webadmin@arch.tamu.edu',
    url = 'https://github.com/TAMUArch/cmsplugin-button',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        'setuptools',
        'django-cms',]
)
