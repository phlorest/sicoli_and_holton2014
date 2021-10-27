from setuptools import setup


setup(
    name='cldfbench_sicoli_and_holton2014',
    py_modules=['cldfbench_sicoli_and_holton2014'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'sicoli_and_holton2014=cldfbench_sicoli_and_holton2014:Dataset',
        ]
    },
    install_requires=[
        'phlorest',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
