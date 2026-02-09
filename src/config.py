"""Load environment variables from secrets.env and expose them as module variables."""

from pathlib import Path

from dotenv import load_dotenv
import os

# Load secrets.env from project root (parent of src/)
_secrets_path = Path(__file__).resolve().parent.parent / "secrets.env"
load_dotenv(_secrets_path)

# RabbitMQ
RABBITMQ_HOST: str = os.environ.get("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT: str = os.environ.get("RABBITMQ_PORT", "5672")
RABBITMQ_USER: str = os.environ.get("RABBITMQ_USER", "guest")
RABBITMQ_PASSWORD: str = os.environ.get("RABBITMQ_PASSWORD", "guest")
RABBITMQ_VHOST: str = os.environ.get("RABBITMQ_VHOST", "receipts")
