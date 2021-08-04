import instaloader
bot = instaloader.Instaloader()
username = "URL HERE"
print(bot.download_profile(username, profile_pic_only=True))
