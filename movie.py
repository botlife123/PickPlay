

class Items:

    def __init__(self, title, genre, item_type, description="",):

        self.title  = title #title of the movie/tv-show
        self.genre = genre #genre of the movie/tv-show
        self.description = description #description of the item
        self.item_type = item_type #the type of the item that is being added either a movie or a tv-show
        self.user_rating = [] #the list of ratings by the user
        self.user_score = 0.0 #score calculated by the users rating

    def addRating(self, score): #users add a rating to the item and the score will be calculated 

        self.user_rating.append(score) #adds the rating to the list
        self.user_score = sum(self.user_rating)/ len(self.user_rating) #calculates the average score of the rating


class List:

    def __init__(self):

        self.item = {} #stores the dict of the items being added 


    def addItem(self, item): #adds the item to the list

        self.item[item.title] = item #stores the dict using a key 
        print(f"{item.title} has been added!") #displays a message if the item has been added

    def getItem(self, title): #gets the item from the list by its id

        return self.item.get(title) #returns if the id is not found
    
    def searchItem(self, keyword): #the users can search the items that has been added 

        keyword = keyword.lower() 

        search_result = [] #the list stores the results 

        for item in self.item.values(): #iterates through the items in the list

            if keyword in item.title.lower() or keyword in item.genre.lower(): #the items: title and genre are being checked if they keyword matches

                search_result.append(item) #adds the keywords that match to the results

        return search_result #all of the items that matched with the keyword are returned
    
    def filterGenre(self, genre): #the users can filter the genre 

        genre = genre.lower()

        result = [] #results list that is going to store the results

        for item in self.item.values(): #iterates through the items in the list

            if item.genre.lower() == genre: #allows for lowercase 

                result.append(item) #adds the fitler genre to the list
    
        return result #returns the result

    def preferences(self, item_type): #the user can preference a genre

        item_type = item_type.lower()

        result = [] #results list stores the results

        for item in self.item.values(): #iterates through the items in the list 

            if item.item_type.lower() == item_type: #allows for lowercase

                result.append(item) #adds the preferenced item to the list 

        return result #returns the result
    
    def showAll(self): #shows all of the items in the list 
 
        return list(self.item.values()) #returns all items in the list 













