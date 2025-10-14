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

