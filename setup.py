import setuptools

with open('README.md', 'r') as fh:
  long_description = fh.read()

setuptools.setup(
  name='getserv',
  version='0.0.1',
  author='Davide Perozzi',
  author_email='myself@davideperozzi.com',
  description='Retrieve a stable server to deploy stuff',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/davideperozzi/getserv',
  packages=setuptools.find_packages(),
  classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
  python_requires='>=3.6',
)