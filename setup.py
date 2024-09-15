from setuptools import setup, find_packages

# requirements.txt 파일에서 의존성 목록을 읽어오기
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='reminder',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'reminder=reminder.main:main',
        ],
    },
)
