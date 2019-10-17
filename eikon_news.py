import eikon as ek
ek.set_app_key('ba4e52456ba64a87be3b82001782535f159b564e')
print(ek.get_news_headlines('R:IBM.N', date_from='2019-09-27T09:00:00', date_to='2019-09-27T10:00:00'))
