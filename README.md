# Raw Data Bot

A simple Telegram bot built with **python-telegram-bot** (async/await) that provides basic `/start` and `/help` commands.

## Features
- Reads the bot token from the `BOT_TOKEN` environment variable.
- Implements `/start` and `/help` commands.
- Dockerized for easy deployment.

## Project Structure
```
raw_data_bot/
├── main.py            # Bot source code
├── Dockerfile         # Docker image definition
├── requirements.txt   # Python dependencies
├── .env.example       # Example environment file
└── README.md          # This file
```

## Prerequisites
- Docker installed on your machine.
- A Telegram bot token. You can obtain one by talking to [@BotFather](https://t.me/BotFather).

## Setup
1. **Clone the repository**
   ```bash
   git clone <repository_url>
   cd raw_data_bot
   ```

2. **Create an environment file**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and replace `your_telegram_bot_token_here` with the token you received from BotFather.

3. **Build the Docker image**
   ```bash
   docker build -t raw_data_bot:latest .
   ```

4. **Run the container**
   ```bash
   docker run -d --name raw_data_bot \
       --env-file .env \
       raw_data_bot:latest
   ```
   The bot will start polling for updates.

## Local Development (without Docker)
If you prefer to run the bot directly on your host:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export BOT_TOKEN=your_telegram_bot_token_here
python -m main
```

## License
This project is licensed under the MIT License.
