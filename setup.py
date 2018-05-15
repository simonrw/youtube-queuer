from __future__ import print_function, division, absolute_import
from setuptools import setup, find_packages

setup(
        name='youtube-queuer',
        description='Download lots of youtube videos',
        version='0.0.1',
        author='Simon Walker',
        author_email='s.r.walker101@googlemail.com',
        packages=find_packages(),
        entry_points={
            'console_scripts': [
                'ytqd=youtube_queuer:ytqd_main',
                'ytq=youtube_queuer:ytq_main',
                'ytq-worker=youtube_queuer:ytq_worker_main',
                ],
            },
        install_requires=[
            'flask',
            'requests',
            'youtube-dl',
            ],
        )
