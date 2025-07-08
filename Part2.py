def get_books():
    num_books = 0

    while True:
        try:
            num_books = int(input('How many books were purchased this month? '))

            if num_books < 0:
                raise ValueError

            break
        except ValueError:
            print('Please enter a number 0 or greater.')

    return num_books

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
    user_books = get_books()

    calculate_points(user_books)

if __name__ == '__main__':main()

    