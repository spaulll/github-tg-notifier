---

# GitHub Webhook to Telegram Notifier

This Python script sets up a webhook server using Flask to listen for GitHub events, specifically push events, and sends notifications to a Telegram account.

## Setup

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/spaulll/github-tg-notifier.git
    ```

2. Install the required Python packages using pip:

    ```bash
    pip install flask requests
    ```

3. Create a Telegram bot and obtain the bot token. You can create a new bot and get the token from [BotFather](https://core.telegram.org/bots#how-do-i-create-a-bot).

4. Get your Telegram chat ID. You can use the `getUpdates` method of the Telegram Bot API or use a bot like `@userinfobot` to get your chat ID.

5. Set up a webhook for your GitHub repository:
   - Go to your repository's settings, then "Webhooks".
   - Add a new webhook with the following settings:
     - Payload URL: `http://your-server-ip:5000/github-webhook`
     - Content type: `application/json`
     - Secret: A random string (keep it secure)
   - Replace `your-server-ip` with the IP address or domain name of the server where you will run this script.

6. Update the script:
   - Open `app.py` and replace the following placeholders:
     - `YOUR_TELEGRAM_BOT_TOKEN` with your Telegram bot token.
     - `YOUR_TELEGRAM_CHAT_ID` with your Telegram chat ID.
     - `YOUR_GITHUB_WEBHOOK_SECRET` with the secret you set up in step 5.

7. Run the script:
   - Run the Flask server using the following command:

     ```bash
     python app.py
     ```

   - Ensure that the script is running on a server with a publicly accessible URL.

8. Test the setup:
   - Push to your GitHub repository and verify that you receive a notification on Telegram.

## Usage

- This script listens for GitHub events, particularly push events, and sends notifications to a specified Telegram chat whenever an event occurs.

## Troubleshooting

- If you encounter any issues or errors, check the console output for error messages.
- Ensure that the webhook URL is correct and reachable from GitHub.

---
