# store-assistant
Simple Store Assistant

## Docker Setup

### Building the Image
```bash
docker build -t store-assistant .
```

### Running the Container
```bash
docker run -d -p 8000:8000 --name store-assistant store-assistant
```

### Environment Variables
The following environment variables can be set when running the container:
- `PORT`: The port to run the application on (default: 8000)
- `HOST`: The host to bind to (default: 0.0.0.0)

### Health Check
The container includes a health check that runs every 30 seconds. The application must implement a `/health` endpoint that returns a 200 status code when healthy.
