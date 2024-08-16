from setuptools import find_packages,setup

setup(
    name='Hr_Analyst',
    version='0.0.1',
    author='Ayan Biswas',
    author_email='biswas.ayan1997@gmail.com',
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)
