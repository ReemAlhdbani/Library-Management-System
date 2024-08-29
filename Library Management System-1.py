


# Initialize the lists for books won and books on the wishlist
library_wons = []
library_wish = []

# Get the first book the user has won
q1_book_won = input("Enter the name of a book you've won: ")
library_wons.append(q1_book_won)

# Get the second book the user has won (optional)
q2_anotherBookSkip = input("Enter the name of another book you've won (or press 'Enter' to skip): ")
if q2_anotherBookSkip:
    library_wons.append(q2_anotherBookSkip)

print(f"Your Library: {library_wons}")

# Get the first book the user wishes to have
q3_BookWish = input("Enter the name of a book you wish to have in the future: ")
library_wish.append(q3_BookWish)

# Get the second book the user wishes to have (optional)
q4_anotherBookSkipWish = input("Enter the name of another book you wish to have (or press 'Enter' to skip): ")
if q4_anotherBookSkipWish:
    library_wish.append(q4_anotherBookSkipWish)

print(f"Your Wishlist: {library_wish}")

# Get the name of a book from the user's wishlist that they've already won
q5_wishlist_won = input("Enter the name of a book from your wishlist that you've already won (or press 'Enter' to skip): ")
if q5_wishlist_won:
    # Update the library list to include the book from the wishlist
    update_library=[]
    update_library.extend(library_wons)
    update_library.append(q5_wishlist_won)
    print(f"Updated Library: {update_library}")

    # Remove the book from the wishlist since the user has already won it
    if q5_wishlist_won in library_wish:
        library_wish.remove(q5_wishlist_won)
        print(f"Updated Wishlist: {library_wish}")
else:
    print("End of questions.")
