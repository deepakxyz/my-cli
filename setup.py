from setuptools import setup
setup(
    name = 'my-cli',
    version = '0.1.0',
    packages = ['cli','non'],
    entry_points = {
        'console_scripts': [
            'cli = cli.__main__:main',
            'non = non.__main__:main',
        ]
    })