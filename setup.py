from setuptools import setup, find_packages

setup(
    name="la_crime",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "jupysql",
        "psycopg2",
        "toml",
        "matplotlib",
        "seaborn",
        "sqlalchemy",
        "scikit-learn",
        "statsmodels",
        "plotly",
        "requests",
        "beautifulsoup4",
        "lxml",
        "ipykernel",
        "ipywidgets",
        "tqdm",
        "joblib",
        "jupyterlab",
    ],
)