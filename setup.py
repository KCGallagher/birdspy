#
# birdspy setuptools script
#

from setuptools import setup, find_packages


def get_version():
    """
    Get version number from the birdspy module.
    The easiest way would be to just `import birdspy`, but note that this may
    fail if the dependencies have not been installed yet. Instead, we've put
    the version number in a simple version_info module, that we'll import here
    by temporarily adding the oxrse directory to the pythonpath using sys.path.
    """
    import os
    import sys

    sys.path.append(os.path.abspath('birdspy'))
    from version_info import VERSION as version
    sys.path.pop()
    return version

def get_readme():
    """
    Load README.md text for use as description.
    """
    with open('README.md') as f:
        return f.read()


setup(
    # Package name
    name='birdspy',

    # Version
    version=get_version(),

    description='This is a image analysis tool for wildlife images',  # noqa

    long_description=get_readme(),

    license='BSD 3-Clause "New" or "Revised" License',

    # author='',

    # author_email='',

    maintainer='',

    maintainer_email='',

    url='https://github.com/KCGallagher/birdspy',

    # Packages to include
    packages=find_packages(include=('birdspy', 'birdspy.*')),
    include_package_data=True,

    # List of dependencies
    install_requires=[
        # Dependencies go here!
        'matplotlib',
        'numpy>=1.8',
    ],
)
