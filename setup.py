from setuptools import setup, find_packages


setup(
    name='FreeStrange',
    version='1.0.1',
    author='CleverCreator',
    author_email='clevercreator@10minutesmail.com',
    packages=find_packages(),
    zip_safe=True,
    platforms=['Linux', 'MacOS'],
    install_requires=[''],
    python_requires='>=3.9',
    description='A unlock data system',
    long_description='Seeing https://github.com/CleverCreater/FreeData',
    license='MIT',
    url='https://github.com/CleverCreater/FreeData',
    classifiers=[],
    scripts=['./entry.py']
)
            