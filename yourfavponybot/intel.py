import random, tweepy

class EvaluationType():
    guess = 1
    twitterFeed = 2

class AI:
    api = None
    ponyLiked = []

    def __init__(self, api):
        self.api = api 
 
    def begin_search_process(self, ponyList, mention):
        pony = ""
        self.ponyLiked = dict() 
        tweets = self.api.user_timeline(id=mention.user.id, count=30)
        for t in tweets:
            for p in ponyList:
                if p in t.text:
                    # TODO add more stuff
                    # TODO move these in a file
                    score = 1
                    text = t.text.split(' ', 1)[1].lower()

                    # We determine by the exciteness-factor
                    # of the user when relating to a specific pony

                    if "cute" in text:
                        score += 2
                    if "awesome" in text:
                        score += 2
                    if "best pony" in text:
                        score += 4

                    if self.ponyLiked.has_key(p):
                        self.ponyLiked[p] += score 
                    else:
                        # Key has to be initialized first
                        self.ponyLiked[p] = score 

        if len(self.ponyLiked) == 0:
            # Welp, until we add more to the search process
            # this is all we got now
            # All we can do is gamble now
            pony = get_rand_pony(ponyList) 
            return pony, EvaluationType.guess
        # Pick the pony with the highest score
        # TODO Since we only pick the first pony
        # there may be multiple ones with the same score
        # Maybe pick a random pony of these?
        pony = max(self.ponyLiked, key=self.ponyLiked.get)
        return pony, EvaluationType.twitterFeed 

def get_rand_pony(ponyList):
    index = random.randrange(0, len(ponyList))
    return ponyList[index]
