# template-srv

This project is a template for developing services for raVioleria16 project. Is based on FastAPI framework and provides a structured approach to building and deploying services.

## Project Structure

The project is organized as follows:

-   `app/`: Contains the main application logic.
    -   `api/`: Defines the FastAPI endpoints for the service.
    -   `config/`: Holds configuration files, such as `app.yaml`, and related functions.
    -   `core/`: Contains the business logic of the service.
    -   `models/`: Defines the data models usedi n the application. 
    -   `providers/`: Manages service providers. It includes a `BaseProvider` abstract class, which is extended by specific provider implementations.
    -   `app.py`: The main FastAPI application file that exposes the service.
-   `deploy_local.sh`: Script for deploying the service locally.
-   `deploy.sh`: Script for deploying the service in a container.
-   `docker-compose.yaml`: Docker Compose configuration for the service.
-   `Dockerfile`: Defines the Docker image for the application.
-   `requirements.txt`: Lists the Python dependencies for the project.

## Deployment

You can deploy the service either locally for development or as a containerized application.

### Local Deployment

To run the service on your local machine, execute the following command:

```bash
./deploy_local.sh
```

### Containerized Deployment

To deploy the service using Docker, use the `deploy.sh` script. You must specify the port on which to expose the service using the `--expose` argument.

```bash
./deploy.sh --expose <PORT>
```

For example, to expose the service on port 8000:

```bash
./deploy.sh --expose 8000
```