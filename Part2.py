# Method used to capture number of books from the user
def get_books(): 
    num_books = 0

    while True: # Holds the user in a loop until user input is valid
        try:
            num_books = int(input('How many books were purchased this month? '))

            if num_books < 0:
                raise ValueError

            break
        except ValueError: # Error presented to user if input is invalid
            print('Please enter a number 0 or greater.')

    return num_books # Returns the inputted number of books

# Takes an integer (the amount of books) and determines amount of points rewarded.
def calculate_points(books): 
    if books == 0:
        print('Points Awarded: 0')
    elif 2 <= books <= 3:
        print('Points Awarded: 5')
    elif 4 <= books <= 5:
        print('Points Awarded: 15')
    elif 6 <= books <= 7:
        print('Points Awarded: 30')
    else:
        print('Points Awarded: 60')

def main():
    user_books = get_books() # Calls method to ask the user for the number of books.

    calculate_points(user_books) # Calls method to determine number of points rewarded and outputs to screen.
    
if __name__ == '__main__':main()

    