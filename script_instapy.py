from instapy import InstaPy
from time import sleep

locations = {
    'goiania': 'c254063/goiania-brazil/',
    'brasil': 'BR/brazil/'
}

tags = ['cidade, dicasdeviagem', 'viagemdossonhos', 'viagemperfeita', 'dicadeviagem', 'fotos', 'fotografia', 'viagem',
'viajemais', 'viajemperfeita', 'viajempelomundo', 'viageminesquecível', 'viajeminesquecível', 'viagemusa', 'fotoviagem']

insta_nicknames = ['vouparaitalia', 'ticobrazileiro', 'qualeasuatrip', 'vemprany', 'orlandoeumbarato', 'omapadaviagem', 
'londrespravoce', 'dicasnovayork', 'tailandiapasseios', 'explorandooglobo', 'idosotambemviaja', 'viajar_e_ser_feliz']

session = InstaPy(username="xxxxx", password="xxxxx")
session.login()
session.set_skip_users(skip_private=False,
                       private_percentage=100,
                       skip_no_profile_pic=True,
                       no_profile_pic_percentage=100,
                       skip_business=True,
                       skip_non_business=False,
                       business_percentage=50,
                       skip_business_categories=[],
                       dont_skip_business_categories=[],
                       skip_bio_keyword=[],
                       mandatory_bio_keywords=[])

session.set_relationship_bounds(enabled=True,
                                potency_ratio=None,
                                delimit_by_numbers=True,
                                max_followers=6000,
                                max_following=6000,
                                min_followers=100,
                                min_following=100,
                                min_posts=2,
                                max_posts=1000)

session.set_action_delays(enabled=True, like=6, randomize=True, random_range_from=70, random_range_to=140)
session.set_action_delays(enabled=True, comment=35, randomize=True, random_range_from=70, random_range_to=140)
session.set_action_delays(enabled=True, follow=25, randomize=True, random_range_from=70, random_range_to=140)
session.set_action_delays(enabled=True, unfollow=5.2, randomize=True, random_range_from=70, random_range_to=140)
session.set_action_delays(enabled=True, story=5.2, randomize=True, random_range_from=70, random_range_to=140)

session.set_user_interact(amount=5, randomize=True, percentage=80)


session.follow_user_followers(insta_nicknames, amount=15, sleep_delay=120, interact=True)
session.like_by_tags(tags, amount=5, skip_top_posts=True)


