import heapq
import movie

class Recommended: 

    def __init__(self, movie, user):

        self.movie = movie #movie list its going to represent the catalog for both the movie and tv-show
        self.user = user #this is where the rating, preference, and filters objects are

    def getScore(self, item):

        score = 0 #default score

        if item.title in self.user.rating: #if the user has rated an item in the list it will check it

            score += self.user.rating[item.title] #it adds the users rating to the title of the item

        if item.genre in self.user.preferenced_genre: #if the user puts a genre as a preference it will check it

            score += 1.0 #it adds a score boost of 1.0 to the preference genre the user picked

        if score  == 0: #if the rating is not found 
 
            score = item.user_score #it will use the other users score

        return score 

    def getRecommendation(self):

        req_heap = [] #recomendation heap

        for item in self.movie.showAll():

            if item.title in self.user.watched: #if the user watched the item it will skip it

                continue

            if item.title in self.user.dnf: #if the user mark it as dnf the item it will skip it

                continue

            if item.genre in self.user.filter_genre: #if the user filted out the genre the item it will skip it

                continue


            score = self.getScore(item) #this is the personalized score the user
            heapq.heappush(req_heap, (-score, item.title, item)) #the highest rated item will be returned first

        result = []

        while req_heap:

            popped = heapq.heappop(req_heap) #it pops the highest item from the heap 
            item = popped[2] #the item is being retrieved from the tuple
            result.append(item) #it adds an item to the results in order(highest goes first then lowest)

        return result
        







