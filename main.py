
from movie import List, Items
from recommend import Recommended 
from users_ import User

def main():

    print("*********************** Welcome To PickPlay! ***************************************")
    print("********************************************************************************")
    print("                     A Movie/Show Reccomendation System"                         )
    print("********************************************************************************")

    name = input("Enter in your name: ") #gets the users name

    user = User(name) #user object 

    movie = List() #list for the movie and tv-show

    recommend = Recommended(movie, user) #recomennder object

    while True: 
        
        #main menu option selections
        print("\n Welcome to the Main Menu")
        print("\n 1. Add Movie/Show")
        print("\n 2. Leave a Rating")
        print("\n 3. Leave a Review")
        print("\n 4. Mark Watched Or DNF(did not finish)")
        print("\n 5.Filter a Genre")
        print("\n 6. Pick a Preference")
        print("\n 7. Search For a Movie/Show")
        print("\n 8. View Your Watch History")
        print("\n 9. View Your Reviews")
        print("\n 10. View Your Rating") 
        print("\n 11. View Your Recs")
        print("\n 12. Exit")

        choice = input("\nEnter in your choices: ") #the user can enter in their choices from the selection 

        #adds a movie or tv-show to the list
        if choice == "1" :

            title = input("Title: ")
            genre = input("Genre: ")
            item_type = input("Item Type: ")
            movie.addItem(Items(title, genre, item_type))

        #rating
        elif choice == "2" :
            
            title = input("Title to rate: ")
            score = float(input("Rating: "))
            user.rate(title, score)

        #review
        elif choice == "3":

            title = input("Title to review: ")
            review = input("Review: ")
            user.createReview(title, review)

        #mark choices
        elif choice == "4" :

            title = input("Title: ")
            pick = input("Mark Show/Movie as watched or dnf: ").lower()

            if pick == "watched":

                user.markWatched(title)

            elif pick == "dnf" :
                
                user.markDNF(title)

            else: 
                print("Pick either Watched or DNF.")

        #filter out a genre
        elif choice == "5" :

            genre = input("Pick a Genre to Filter Out: ")
            user.filterGenre(genre)

        #user preference
        elif choice == "6" :

            genre = input("Which Genre Do you Prefer: ")
            user.addPreference(genre)

        #search for a movie/show
        elif choice == "7": 

            keyword = input("Search: ")
            result = movie.searchItem(keyword)

            if result:

                for item in result:

                    print(f"{item.title}, {item.genre}, {item.item_type}, {item.user_score}") #prints the results

            else:
                print("No results popped up.") #if no result has shown when entering in the item to be search a message appears

        #view watch history
        elif choice == "8" :
            
            user.viewHistory()

        #view rating history
        elif choice == "9" :

           user.viewReview()

        #view review history
        elif choice == "10":

            user.viewRating()


        #view recs
        elif choice == "11" :

            result = recommend.getRecommendation()

            print(f"These are the Recs for {user.name}: ") #shows the recommendation for the user 

            if result:

                i = 1
                for item in result:

                    print(f"{i} {item.title}, {item.genre}, Score: {item.user_score}")#prints out the recommendation for the user 
                    i += 1 

            else:
                print("There are currently no recommendations.") #if there are no recommendations then a message appears

        #exit
        elif choice == "12" :

            print(f"\nExiting...Bye {user.name} Enjoy Watching!") #exit message when the user wishes to exit 

            break

        else:
            print("Please Enter Between (1-12)") #if the user enters in numbers not provided in the list it will show this message 

main()





        





            









    


        
