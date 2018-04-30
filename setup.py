from setuptools import setup, find_packages

with open('requirements.txt') as fp:
    install_requires = fp.read()


setup(
      name='apidoc',
      version='1.1',
      description='Devops Analytics',
      author='Elias Costa',
      author_email='elias.costa@portalunimed.com.br',
      py_modules=['run', 'apidoc'],
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Programming Language :: Python :: 3.6'
      ],
      project_urls={
            'Source': 'https://gitlab.portalunimed.com.br/microservices/apidocs-build',
      },
      python_requires='>=3',
      packages=find_packages(),
      install_requires=install_requires
)

