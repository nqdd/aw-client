from aw_core.config import load_config_toml

default_config = """
[server]
hostname = "tracker.komu.vn"
port = "5600"
secret = "secret"

[client]
commit_interval = 300

[server-testing]
hostname = "127.0.0.1"
port = "5666"

[client-testing]
commit_interval = 5
""".strip()


def load_config():
    return load_config_toml("aw-client", default_config)
