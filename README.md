# Telegram-chat-summary
[Side Project]. If you are bored by telegram group chats, try to summarize
chat to see how would your friends would react to your messages.

## Atleast you will have some fun

# Thanks to these repos (I simply copied code from minGPT)

    1. (MinGPT)[https://github.com/karpathy/minGPT]

    2. (TeleBot)[https://github.com/KyleJamesWalker/telebot]

## Usage:
1. Gather data - (Export Group chat from Telegram)[https://telegram.org/blog/export-and-more#:~:text=To%20use%20this%20feature%2C%20make,parts%20of%20their%20messaging%20history.]
2. Put chat export folder to chat folder
3. Run `python parse_telegram.py` to parse html message chat to txt file
4. Run `python train.py` (Need big GPU for cuda acceleration)
5. Create Telegram bot
6. Copy `config.ini.default` to `config.ini`. And set [TELEGRAM][secret] to telegram bot api_key.
7. Run `python bot.py` to run bot
8. Enjoy the bot