from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='xemonity',
  version='1.0',
  author='murzik_kukushnik',
  author_email='siniykoshara@gmail.com',
  description='Libraly for simple menu with chosing',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/MurzikYEET/Xemonity',
  packages=find_packages(),
  install_requires=['pynput'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='menu choose choice',
  project_urls={
    "GitHub" : "https://github.com/MurzikYEET/Xemonity"
  },
  python_requires='>=3.6'
)