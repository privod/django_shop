from setuptools import setup, find_packages
from os.path import join, dirname

import project

setup(
    name='django_shop',
    version=project.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),

    install_requires=[
        'Django==1.9.7',
        'Pillow==5.0.0',
        'celery==3.1.18',
        'django-paypal',
    ],
    # entry_points={
        # 'console_scripts': [
            # 'django_shop = project.myshop.manage:main',
        # ]
    # },
    # include_package_data=True,
    # test_suite='tests',
)
