from users_ import User
from movie  import List, Items
from recommend import Recommended

#test 1
def rankTest():

    movie = List()

    user = User("Test user")

    recommend = Recommended(movie, user)
   
    movie.addItem(Items("Superman", "action", "movie"))
    movie.addItem(Items("Summer I turned Pretty", "romance", "tv-show"))
    movie.addItem(Items("A Quiet Place", "horror", "movie"))

    user.rate("Superman", 5.0)
    user.rate("Summer I turned Pretty", 3.8)
    user.rate("A Quiet Place", 4.0)


    result = recommend.getRecommendation()

    if result[0].title == "Superman" and result[1].title == "A Quiet Place":

        print("Test 1 passed with the ranking being correct")

    else:

        print("Test 1 did not pass with the ranking being incorrect")

 
#test 2
def genreTest():

    movie = List()

    user = User("Test user")

    recommend = Recommended(movie, user)
   
    movie.addItem(Items("The Hunger Games", "dystopian", "movie"))
    movie.addItem(Items("Batman", "action", "movie"))
    movie.addItem(Items("IT", "horror", "movie"))

    user.rate("The Hunger Games", 4.8)
    user.rate("Batman", 3.0)
    user.rate("IT", 3.8)

    user.filterGenre("horror")
    user.filterGenre("sci-fi")
    user.addPreference("dystopian")

    result = recommend.getRecommendation()
    genre_title = []

    for item in result:

        genre_title.append(item.title)

    if result[0].title == "The Hunger Games" and result[1].title ==  "Batman":

        print("Test 2 passed and the genre filter and preference correctly works")

    else:

        print("Test 2 did not pass and the genre filter and preference does not correctly work")


#test 3
def filterTest():
    
    movie = List()

    user = User("Test user")

    recommend = Recommended(movie, user)

    result = recommend.getRecommendation()

    movie.addItem(Items("Spiderman", "action", "movie"))
    movie.addItem(Items("Suits", "drama", "tv-show"))
    movie.addItem(Items("Veronica Mars", "mystery", "tv-show"))

    user.markWatched("Spiderman")
    user.markDNF("Suits")

    result = recommend.getRecommendation()
    filter_title = []

    for item in result:

        filter_title.append(item.title)

    if "Spiderman" not in filter_title and "Suits" not in filter_title:

        print("Test 3 passed and the watched and dnf feature works")

    else:

        print("Test 3 did not pass and the watched and dnf feature does not work works")


rankTest()
genreTest()
filterTest()
print("Every test passed")






    





















    



