from setuptools import setup, find_packages

setup(
    name='RF_CICD_TEST',  # Replace with your package name
    version='0.1.0',           # Replace with your package version
    description='Creating mlpipieline using mlflow and github actions to deployt it in aws ec2 or sagemakweer',  # Replace with your package description
    long_description=open('README.md').read(),  # Make sure to have a README.md file
    long_description_content_type='text/markdown',
    author='Vamsidhar Y',        # Replace with your name
    author_email='yvdhars@gmail.com',  # Replace with your email
    url='https://github.com/yvdhars/RF_cicd_test',  # Replace with your project's URL
    package_dir={'': 'src'},  # Tell setuptools where to find packages
    packages=find_packages(where='src'),  # Find packages in the 'src' directory

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    python_requires='>=3.6',  # Adjust based on your package requirements
    include_package_data=True,
)
