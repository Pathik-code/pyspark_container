# PySpark Container Project

## Overview
A containerized PySpark environment for data analysis with a master node and two worker nodes. Currently configured to analyze organization data from a CSV file.

## Project Structure
```
pyspark_container/
├── Dockerfile              # Uses apache/spark:3.4.1-python3 base image
├── docker-compose.yml      # Defines 4 services: master, 2 workers, and pyspark client
├── requirements.txt        # Python dependencies
├── start-spark.sh         # Startup script for Spark services
├── src/
│   └── main.py            # Sample analysis script
└── data/
    └── ShopBusinessCsv/   # Contains organizations data
```

## Quick Start
1. Build and start containers:
```bash
docker compose up --build
```

2. Access UIs:
- Spark Master: http://localhost:8080
- Spark Worker 1: http://localhost:8081
- Spark Worker 2: http://localhost:8082
- PySpark App: http://localhost:5057

## Current Analysis Features
- Total record count
- Column count
- Top 10 Industries by company count
- Top 10 Countries by average employee count

## Configuration
### Service Ports
- Spark Master: 7077 (internal), 8080 (UI)
- Worker 1: 8081 (UI)
- Worker 2: 8082 (UI)
- PySpark App: 5057 (mapped from 4040)

### Resources
- Workers: 1 core, 1GB memory each
- Healthchecks enabled for all services
- Auto-restart enabled

### Environment
- Java 11 with module access fixes
- Python 3.9
- PySpark 3.4.1
- Netcat for healthchecks

## Notes
- Uses bridge network 'spark-net'
- Volume mounts for src and data directories
- Configured for JVM module access
- Healthchecks ensure proper service startup


# PySpark Container Project

## Available UIs
- Spark Master UI: http://localhost:8080
- Spark Worker 1 UI: http://localhost:8081
- Spark Worker 2 UI: http://localhost:8082
- PySpark Application UI: http://localhost:5057

## Quick Start

1. Start the containers:
```bash
docker compose up --build -d
```

2. Wait for all services to be healthy (about 30 seconds)

3. Access the PySpark container and run the analysis:
```bash
# Enter the PySpark container
docker exec -it pyspark_container-pyspark-1 bash

# Inside the container, run the analysis script
python3 /app/src/main.py
```

4. View the results:
- Check the console output for analysis results
- Access the Spark UI at http://localhost:5057 to see job details
- Press Enter in the console to exit the application

## Analysis Features
- Total record count
- Column count
- Top 10 Industries by company count
- Top 10 Countries by average employee count

## Notes
- The script will keep running until you press Enter to allow exploring the Spark UI
- If you need to rerun the analysis, just execute step 3 again 
