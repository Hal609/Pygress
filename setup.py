from setuptools import setup, find_packages

setup(
    name='pygress',
    version='0.1',
    packages=find_packages(),
    description='A simple progress bar for loops',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Hal Kolb',
    author_email='hal@kolb.com',
    url='https://github.com/Hal609/pygress',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)