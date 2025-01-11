from setuptools import setup, find_packages

setup(
    name='interface_testing',
    version='0.1.0',
    author='R Nishanth',
    author_email="nishanth0962333@gmail.com"
    packages=find_packages(),
    install_requires=[
        'flask',
        'torch',
        'transformers',
        'nltk',
        'janome',
        'requests'
    ],
    include_package_data=True
)
