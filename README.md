# install libraries on ec2
pip3 install --user pytz
pip3 install --user requests

# Setup telegram to retrieve chat_id, create bot and get token
follow - https://stackoverflow.com/a/67152755

# Steps
1. Add list of pin codes in `pin_codes` variable
2. Update `telegram_token`
3. Update `chat_ids`. You can list multiple chat ids to receive messages to multiple telegram recipients.
