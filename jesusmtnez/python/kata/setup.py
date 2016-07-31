try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'The Bowling Scoring Kata',
    'author': 'Jesús Martínez-Barquero Herrada',
    'author_mail': 'jesusmartinez93@gmail.com',
     # 'url': '',
    'version': '0.0.1',
    'install_requires': [],
    'packages': [],
    'scripts': [],
    'name': 'bowling_scoring_kata'
}

setup(**config)
