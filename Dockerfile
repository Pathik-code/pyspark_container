FROM apache/spark:3.4.1-python3

USER root

# Install netcat for healthcheck
RUN apt-get update && \
    apt-get install -y netcat-traditional && \
    rm -rf /var/lib/apt/lists/*

# Install additional Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the startup script
COPY start-spark.sh /
RUN chmod +x /start-spark.sh

WORKDIR /app

# Set default command
ENTRYPOINT ["/start-spark.sh"]
