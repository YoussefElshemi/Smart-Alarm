import setuptools

long_description = open('README.md', 'r').read()

setuptools.setup(
    name='COVID-19 Smart Alarm Clock',
    version='0.0.1',
    author='Youssef Elshemi',
    author_email='ye216@exeter.ac.uk',
    description='COVID-19 Smart Alarm Clock',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.8.3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8.3',
)