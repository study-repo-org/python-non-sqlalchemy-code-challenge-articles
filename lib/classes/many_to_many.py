class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be between 5 and 50 characters, inclusive")
        
        self.__author = author
        self.__magazine = magazine
        self.__title = title
        Article.all.append(self)
        magazine._add_article(self)
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
        if not isinstance(new_author, Author):
            raise ValueError("New author must be an instance of Author")
        self.__author._remove_article(self)
        self.__author = new_author
        new_author._add_article(self)

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("New magazine must be an instance of Magazine")
        self.__magazine._remove_article(self)
        self.__magazine = new_magazine
        new_magazine._add_article(self)


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self.__name = name
        self.__articles = []

    @property
    def name(self):
        return self.__name

    def articles(self):
        return self.__articles

    def magazines(self):
        return list(set([article.magazine for article in self.__articles]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def _add_article(self, article):
        self.__articles.append(article)

    def _remove_article(self, article):
        self.__articles.remove(article)

    def topic_areas(self):
        if not self.__articles:
            return None
        return list(set([article.magazine.category for article in self.__articles]))


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not isinstance(category, str):
            raise ValueError("Name and category must be strings")
        if len(name) < 2 or len(name) > 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self.__name = name
        self.__category = category
        self.__articles = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("Name must be a string")
        if len(new_name) < 2 or len(new_name) > 16:
            raise ValueError("Name must be between 2 and 16 characters, inclusive")
        self.__name = new_name

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            raise ValueError("Category must be a string")
        if len(new_category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self.__category = new_category

    def articles(self):
        return self.__articles

    def contributors(self):
        return list(set([article.author for article in self.__articles]))

    def _add_article(self, article):
        self.__articles.append(article)

    def _remove_article(self, article):
        self.__articles.remove(article)
