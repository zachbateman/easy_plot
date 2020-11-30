from distutils.core import setup

with open('README.md', 'r') as f:
    long_description = f.read()

VERSION = '0.1.0'

setup(name='statplot',
      version=VERSION,
      packages=['statplot'],
      license='MIT',
      author='Zach Bateman',
      description='Easy Statistical Visualization',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/zachbateman/statplot.git',
      download_url='https://github.com/zachbateman/statplot/archive/v_' + VERSION + '.tar.gz',
      keywords=['STATISTICS', 'VISUALIZATION', 'SIMPLE', 'EASY', 'PLOT'],
      install_requires=['matplotlib', 'seaborn', 'pandas'],
      classifiers=['Development Status :: 3 - Alpha',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Programming Language :: Python :: 3.9',
                   ]
)
