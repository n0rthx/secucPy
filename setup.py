from setuptools import setup, find_packages 



setup(

    name='secucPy',
    version='0.1',
    license='MIT',
    author="Furkan Aslan",
    author_email='furkanaaslan@protonmail.com',
    packages=find_packages('secucpy'),
    package_dir={'': 'secucpy'},
    url='https://github.com/n0rthx/secucpy',
    keywords='Socket creator',
    install_requires=[
          'numba',
      ],

)