class Library:
    def __init__(self):
        pass    
        books={"Atomic Habits":450,
               "Rich dad Poor dad":350,
               "The Psychology of Money":399,
               "Ikigai":299,
               "Deep work":399,
               "The alchemist":299,
               "Think and Grow rich":250,
               "zero to one":350,
               "clean code":650,
               "python crash course":550,
               "The pragmatic Programmer":700,
               "Harry Potter":499,
               "The silent Patient":350,
               "1984":299,
               "The great Gatsby":250,
               }
    def display_options(self):
        print("BOOKVAULT v1.0")
        print("LIBRARY MANAGEMENT SYSTEM")
        print("-"*60)
        print("1. Book Management\n2. Member Management\n3. Issue a Book\n4. Return a Book\n5. Search Books\n6. Library Reports\n7. Exit")
        print("-"*60)
        # print("-"*60)
        choice=input("enter your choice")
    # def 
libs=Library()
libs.display_options()