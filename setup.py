from setuptools import setup, find_packages

VERSION = '0.2.5'
DESCRIPTION = 'PyToolBelt - Extend your built-in methods.'
LONG_DESCRIPTION = open('README.md', 'r').read()

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="py_toolbelt",
        version=VERSION,
        author="Soami Charan",
        author_email="charansoami@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        license='MIT',
        packages=find_packages(),
        install_requires=['forbiddenfruit', 'jsondatabase', 'future'],
        keywords=['python', 'PyToolBelt'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
        ]
)
