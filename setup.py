from setuptools import setup, find_packages

setup(
    name='praktikos',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyautogui==0.9.52',
        'opencv-python-headless==4.5.3.56',
        'pandas==1.3.3',
        'Pillow==8.3.1',
        'mss==6.2.2',
        'tesseract==0.1.3',
    ],
    entry_points={
        'console_scripts': [
            'praktikos = praktikos.main:main'
        ]
    },
    license='MIT',
    author='Jack Kitto',
    author_email='jack.kitto@gmail.com',
    description='PRAKTIKOS: Python-based RPA framework'
)
