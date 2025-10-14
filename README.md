# SchwabTraderWebApp
A containerized Python web application designed to run alongside a trader’s database, database management interface, and secrets vault. All services communicate securely over a private Docker network, making this project intended for personal, self-hosted use.

To configure:
In a terminal, from the project directory, run docker compose -up  *docker-compose.yml*

This will ensure the containers for the following modules are properly configured for the app to run:
- Database (PostgreSQL database)
- Database Manager (pgAdmin)
- Secrets Manager (Docker Secrets)
- Application code (Flask Python framework)
- WSGI interface (Caddy WSGI)

APPLICATION CODE:
The application runs as a package, beginning from the top-level __init__.py file. This file instantiates the Flask application object and registers all blueprints.

-- APIS:
    APIs are at the heart of the application's core functionalities. Modularizing the application's main functions allows for ease of development and reusage of redundant code.
    The following APIs serve the Schwab Trader Web Application's core functions:
        - AUTH - ensures authentication and authorization for those looking to secure their use of the web application. Allows for the creation of users and delegated access control using roles and permissions as defined by default RBAC policies.
        - GUI - centralizes redundant code to properly display data from various APIs in consistent manners. Does not route much, but returns graphical objects for display on the GUI.
        - MARKETS - facilitates reading and writing of market data from both the user's designated database, and external free data sources (such as yfinance).
        - ML - interfaces machine learning models with various data sets returned from other APIs. Does not route much, but returns strategy signals, numerical analyses/statistics, and interacts with graphical objects.
        - SCHWAB - bridges API calls from the user to the Schwab Developer API given the user has supplied API tokens and has the necessary permissions/access from Schwab.
        - TRADER - records a trader's progress (trades, journal entries, strategy usage/execution) for historical tracking within the web application.
