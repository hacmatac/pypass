from setuptools import setup

setup(
    name='pypass',
    version='0.1',
    py_modules=['pypass', 'password'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pypass=pypass:cli
    ''',
)
