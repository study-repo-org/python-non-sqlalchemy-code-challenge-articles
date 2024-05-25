class Article:
    def __init__(self, author, magazine, title):
        # Checking if author is an instance of Author
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author")
        # Checking if magazine is an instance of Magazine
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        # Checking if title is a string
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        # Checking if title is between 5 and 50 characters
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters, inclusive")
        # Assigning author, magazine, and title to private variables
        self.__author = author
        self.__magazine = magazine
        self.__title = title

    @property
    def title(self):
        # Returning the private title variable
        return self.__title
    


class Author:
    def __init__(self, name):
        # Checking if name is a string
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        # Checking if name is longer than 0 characters
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        # Assigning name to a private variable
        self.__name = name

    @property
    def name(self):
        # Returning the private name variable
        return self.__name

    

class Magazine:
    def __init__(self, name, category):
        # Checking if name and category are strings
        if not isinstance(name, str) or not isinstance(category, str):
            raise ValueError("Name and category must be strings")
        # Checking if name is between 2 and 16 characters
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        # Checking if category is longer than 0 characters
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        # Assigning name and category to private variables
        self.__name = name
        self.__category = category

    @property
    def name(self):
        # Returning the private name variable
        return self.__name

    @name.setter
    def name(self, new_name):
        # Checking if new name is a string
        if not isinstance(new_name, str):
            raise ValueError("Name must be a string")
        # Checking if new name is between 2 and 16 characters
        if len(new_name) < 2 or len(new_name) > 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        # Assigning new name to the private variable
        self.__name = new_name

    @property
    def category(self):
        # Returning the private category variable
        return self.__category

    @category.setter
    def category(self, new_category):
        # Checking if new category is a string
        if not isinstance(new_category, str):
            raise ValueError("Category must be a string")
        # Checking if new category is longer than 0 characters
        if len(new_category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        # Assigning new category to the private variable
        self.__category = new_category

