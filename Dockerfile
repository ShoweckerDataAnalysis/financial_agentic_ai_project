# Start from official n8n image
FROM n8nio/n8n:latest

# Start from official n8n image
# FROM n8nio/n8n:latest

USER root

#Install Python, pip, and dev libraries
RUN apk add --no-cache \
    python3 \
    py3-pip \
    py3-virtualenv \
    gcc \
    musl-dev \
    libffi-dev \
    freetype-dev \
    libpng-dev \
    build-base

# Create a virtual environment
RUN python3 -m venv /opt/pyenv

# Install Python packages inside the virtual environment
RUN /opt/pyenv/bin/pip install --no-cache-dir pandas yfinance matplotlib seaborn numpy

# Set the PATH so scripts can use the virtual environment by default
ENV PATH="/opt/pyenv/bin:$PATH"

USER node

# Optional: Create a virtual environment to isolate Python execution (good for agents later)
# RUN python3 -m venv /opt/pyenv
# ENV PATH="/opt/pyenv/bin:$PATH"

# Everything else remains the same