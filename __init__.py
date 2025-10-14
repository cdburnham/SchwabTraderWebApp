from flask import Flask
app = Flask(__name__)

"""
# Import routes for the following APIs:

- GUI API
    Handles proper display of data received from data and machine learning APIs.
    Does not require routing. Returns graphical objects to display on the front end.
- AUTH API
    Handles login, session management and RBAC.
    Routes: register, login, logout.
- SCHWAB API
    Handles all communications with the user's Schwab account(s).
- TRADER API
    Handles web-app based tracking of trader information such as trades taken, research
    write-ups, and strategy implementation.
- MARKETS API
    Handles market data read/write operations and market data display objects.
- MACHINE LEARNING API
    Handles all machine learning (ML) model applications to relevant data and ML model
    interfacing with the GUI.

"""

from SchwabTraderWebApp.apis.gui.routes import gui_api
from SchwabTraderWebApp.apis.auth.routes import auth_api
from SchwabTraderWebApp.apis.schwab.routes import schwab_api
from SchwabTraderWebApp.apis.trader.routes import trader_api
from SchwabTraderWebApp.apis.markets.routes import  markets_api
from SchwabTraderWebApp.apis.ml.routes import machine_learning_api

"""
Register API blueprints.
"""

app.register_blueprint(gui_api)
app.register_blueprint(auth_api)
app.register_blueprint(schwab_api)
app.register_blueprint(trader_api)
app.register_blueprint(markets_api)
app.register_blueprint(machine_learning_api)