"""Counter service package."""
from flask import Flask

app = Flask(__name__)

from service import routes  # noqa: F401, E402
