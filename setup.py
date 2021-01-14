from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = 'PyToolBelt - Extend your built-in methods.'
LONG_DESCRIPTION = ''

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="py_toolbelt",
        version=VERSION,
        author="Soami Charan",
        author_email="charansoami@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['forbiddenfruit'],
        keywords=['python', 'PyToolBelt'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
        ]
)
