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
                'ytld=youtube_queuer:ytld_main',
                'yt-init=youtube_queuer:db_init',
                ],
            },
        )
