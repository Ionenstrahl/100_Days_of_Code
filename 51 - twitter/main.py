from internetSpeedTwitterBot import InternetSpeedTwitterBot as Bot

Bot = Bot()
Bot.get_internet_speed()
if Bot.check_slow_internet():
    Bot.tweet_at_provider()
