
class User:

    def __init__(self, name, description = ""):

        self.name = name #the users name
        self.watched = set() #user watched the item
        self.dnf = set() #user dnf the item
        self.rating = {} #user rating
        self.description = description #description of the item
        self.review = {} #user review
        self.preferenced_genre = set() #user sets a preference on the genre
        self.filter_genre = set() #user filters out a genre

    def rate(self, title, score): #iterates through the ratings score

        if 1 <= score <= 5: #the score it out of 5 and it checks if the score is between 1-5

            self.rating[title] = score #stores the users score 

            print(f"Rating {title}: {score}/5") #prints the score out of 5

        
    def createReview(self, title, review): #users have the ability to create reviews 

        self.review[title] = review #stores the users review

        print(f"Review for: {title}") #prints the review for the specific title the user enters in 

    def markWatched(self, title): #users have the ability to mark the item as watched

        self.watched.add(title) #the user adds the title of the watched item 
        self.dnf.discard(title) #prevents the titles from being both watched and dnf 
        print(f"Watched: {title}" ) #prints the watched result


    def markDNF(self, title):#users have the ability to mark the item as dnf

        self.dnf.add(title) #the user adds the title of the dnf item 
        self.watched.discard(title) #prevents the titles from being both watched and dnf 
        print(f"DNF: {title}") #prints the watched result

    def addPreference(self, genre): #users have the ability to add a preference to a genre

        self.preferenced_genre.add(genre.lower()) #the user adds the preferenced genre item

        print(f"{genre} is added to Preference") #prints the genre that is preferenced by the user


    def filterGenre(self, genre): #the user filters out the genre that they don't want to see

        self.filter_genre.add(genre.lower()) #adds the filtered genre to the list 

        print(f"genre is filtered out" ) #prints out the genre that is filtered out by the user


    def viewHistory(self): #views the watch history of the user 

        print(f"{self.name}'s Watch History") #gets the name of the users and prints the name and their watch history
        print("Watched: ") #displays the watched item
        
        for title in self.watched: #iterates throught the items that are watched
            print(f" - {title}")

        print("DNF: ")

        for title in self.dnf: #iterates throught the items that are dnfed
            print(f" - {title}")

            
    def viewRating(self): #views the rating history of the user 

        print(f"{self.name}'s Ratings") #gets the name of the users and prints the name and their rating

        for  title , score in self.rating.items(): #iterates throught the items that have a rating

            print(f" {title}: {score}/5") #displays the score out of 5

            if title in  self.review: #displays the review if the user has left a rating on the specific item

                print(f" Reveiew: {self.review[title]}")


    def viewReview(self): #views the review history of the user 

        print(f"{self.name}'s Review") #gets the name of the users and prints the name and their review

        for title, review in self.review.items(): #iterates throught the items that have a review

            print(f" {title}") #displayst the title that has a review

            if title in self.review: #displays the review if the user has left a rating on the specific item

                print(f"{title}: {review}")



        








    



    





        






