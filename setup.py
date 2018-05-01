from setuptools import setup, find_packages

with open('requirements.txt') as fp:
    install_requires = fp.read()


setup(
      name='gitlab-extraction',
      version='0.1.0',
      description='Gitlab Extraction for get metrics from development team',
      author='Elias Costa',
      author_email='elias.desenv@gmail.com',
      py_modules=['run', 'gitlab', 'api_resource', 'elasticsearch'],
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Programming Language :: Python :: 3.6'
      ],
      project_urls={
            'Source': 'https://github.com/eliasdesenv/gitlab-extraction/',
      },
      python_requires='>=3',
      packages=find_packages(),
      install_requires=install_requires
)

