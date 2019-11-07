from setuptools import setup

setup(
    name='CloudWebsiteAssignment3',
    packages=['CloudWebsiteAssignment3'],
    install_requires=[
        'flask',
        'flask-login',
        'flask-marshmallow',
        'marshmallow-sqlalchemy',
        'flask-sqlalchemy',
        'flask-security',
        'PyMySQL',
        'wtforms',
        'requests'
    ]
)
