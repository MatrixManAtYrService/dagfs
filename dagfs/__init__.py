import pkg_resources

__version__ = pkg_resources.get_distribution('dagfs').version

def get_provider_info():
    return {
        "package-name": "airflow-provider-dagfs",
        "name": "dagfs",
        "description": "A dependency-aware 'filesystem' for use with Apache Airflow",
        "hook-class-names": ["dagfs.hooks.fsmanip.Unpack", "dagfs.hooks.fsmanip.Pack"],
        "versions": [__version__]
    }
