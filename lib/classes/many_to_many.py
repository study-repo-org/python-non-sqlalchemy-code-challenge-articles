class Article:
    all = []

    def __init__(self, author, magazine, title):
        # Checking if author is an instance of Author
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author")
        # Checking if magazine is an instance of Magazine
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        # Checking if title is a string and its length is within the specified range
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters, inclusive")
        
        # attributes for author, magazine, and title
        self.__author = author
        self.__magazine = magazine
        self.__title = title
        
        # Adding the article to the list of all articles
        Article.all.append(self)
        
        # Adding the article to the magazine's list of articles
        magazine._add_article(self)
        
        # Adding the article to the author's list of articles
        author._add_article(self)

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def magazine(self):
        return self.__magazine

    @author.setter
    def author(self, new_author):
        # Checking if the new author is an instance of Author
        if not isinstance(new_author, Author):
            raise ValueError("New author must be an instance of Author")
        # Remove the current article from the previous author's list of articles
        self.__author._remove_article(self)
        # Sating the new author
        self.__author = new_author
        # Adding the current article to the new author's list of articles
        new_author._add_article(self)


    @magazine.setter
    def magazine(self, new_magazine):
        # Checking if the new magazine is an instance of Magazine
        if not isinstance(new_magazine, Magazine):
            raise ValueError("New magazine must be an instance of Magazine")
        # Remove the current article from the previous magazine's list of articles
        self.__magazine._remove_article(self)
        # Sating the new magazine
        self.__magazine = new_magazine
        # Adding the current article to the new magazine's list of articles
        new_magazine._add_article(self)


class Author:
    def __init__(self, name):
        # Checking if the name is a string and its length is greater than 0
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        # attributes for name and list of articles
        self.__name = name
        self.__articles = []

  
    @property
    def name(self):
        return self.__name

    # Method to return the list of articles written by the author
    def articles(self):
        return self.__articles

    # Method to return the list of magazines the author has contributed to
    def magazines(self):
        return list(set([article.magazine for article in self.__articles]))

    # Method for adding a new article written by the author
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    # Internal method for adding an article to the author's list of articles
    def _add_article(self, article):
        self.__articles.append(article)

    # Internal method for removing an article from the author's list of articles
    def _remove_article(self, article):
        self.__articles.remove(article)

    # Method to return the list of unique topic areas covered by the author's articles
    def topic_areas(self):
        if not self.__articles:
            return None
        return list(set([article.magazine.category for article in self.__articles]))


class Magazine:
    def __init__(self, name, category):
        # Checking if name and category are strings and their lengths are within the specified range
        if not isinstance(name, str) or not isinstance(category, str):
            raise ValueError("Name and category must be strings")
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        # attributes for name, category, and list of articles
        self.__name = name
        self.__category = category
        self.__articles = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        # Checking if the new name is a string and its length is within the specified range
        if not isinstance(new_name, str):
            raise ValueError("Name must be a string")
        if len(new_name) < 2 or len(new_name) > 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        # Sating the new name
        self.__name = new_name

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, new_category):
        # Checking if the new category is a string and its length is greater than 0
        if not isinstance(new_category, str):
            raise ValueError("Category must be a string")
        if len(new_category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        # Sating the new category
        self.__category = new_category

    # Method to return the list of articles published by the magazine
    def articles(self):
        return self.__articles

    # Method to return the list of unique authors who have contributed to the magazine
    def contributors(self):
        return list(set([article.author for article in self.__articles]))

    # Internal method for adding an article to the magazine's list of articles
    def _add_article(self, article):
        self.__articles.append(article)

    # Internal method for removing an article from the magazine's list of articles
    def _remove_article(self, article):
        self.__articles.remove(article)
