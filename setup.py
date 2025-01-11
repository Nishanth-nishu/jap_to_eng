from setuptools import setup, find_packages

setup(
    name='jap-to-eng-project',
    version='0.1.0',
    author='R Nishanth',
    author_email='nishanth0962333@gmail.com',
    description='A data pipeline for model training and prediction',
    packages=find_packages(),
    install_requires=[
        "torch",
        "transformers",
        "scikit-learn",
        "tqdm",
        "logging",
        "flask",
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
