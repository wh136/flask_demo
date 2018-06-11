# coding:utf8
from setuptools import setup, find_packages

setup(
    name='app',
    version='0.0.1',
    packages=find_packages(),  # 包括在安装包内的Python包
    include_package_data=True,  # 启用清单文件MANIFEST.in
    zip_safe=False,
    install_requires=[  # 依赖列表
        'flask',
        'requests',
        'flask-session',
        'flask-mongoengine',
        'redis',
        'celery',
    ]
)
