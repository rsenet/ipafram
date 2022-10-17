from setuptools import setup, find_packages

long_description = "ipafram is a simple utility allowing to identify if a framework has been used to create iOS IPA application"

setup(
    name="ipafram",
    version="0.1",
    description="iOS Framework Identifier",
    long_description=long_description,
    url="https://github.com/rsenet/ipafram",
    author="Régis SENET",
    author_email="regis.senet@orhus.fr",
    license="GPLv3",

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Operating System :: MacOS'
        'Topic :: Utilities',
        'Topic :: Security',
    ],

    packages=find_packages(),

    python_requires='>3.6',

    scripts=['ipafram.py'],
)
