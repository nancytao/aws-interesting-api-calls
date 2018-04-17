from setuptools import setup, find_packages

setup(name='aws_interesting_api_calls',
    version='0.1',
    description='Module inventorying AWS API calls of significance to security',
    url='https://github.com/jchrisfarris/aws-interesting-api-calls',
    author='Chris Farris',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False)