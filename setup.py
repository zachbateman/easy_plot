from distutils.core import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(name='statplot',
      version='0.1.0',
      packages=['statplot'],
      license='TODO',
      author='Zach Bateman',
      description='Easy Statistical Visualization',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/zachbateman/statplot.git',
      download_url='https://github.com/zachbateman/statplot/archive/v_0.1.0.tar.gz',
      keywords=['STATISTICS', 'VISUALIZATION', 'SIMPLE', 'EASY', 'PLOT'],
      install_requires=[],  # TODO
      classifiers=['Development Status :: 3 - Alpha',
                   # 'License :: OSI Approved :: XXX License',  # TODO
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   ]
)
