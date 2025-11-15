# Step 1

BotFather -> new both


get bot API token: put in token.txt

# Step 2

Add bot to group chat
Open group chat via telegram web. Copy chat ID and put in correct place in code / env.

# Step 3
Run in a crontab:


crontab -e
and then

*/30 8-22 * * * /home/<user>/yad2-scraper/run.sh