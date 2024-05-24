class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title length must be between 5 and 50 characters")
        self._title = title
        self.author = author
        self.magazine = magazine
        author.articles_list.append(self)
        magazine.articles_list.append(self)
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise ValueError("Author must be of type Author")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("Magazine must be of type Magazine")
        self._magazine = new_magazine


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name
        self.articles_list = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self.articles_list

    def magazines(self):
        return list(set([article.magazine for article in self.articles_list]))

    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        return list(set([article.magazine.category for article in self.articles_list])) if self.articles_list else None


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not isinstance(category, str):
            raise ValueError("Category must be a string")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name length must be between 2 and 16 characters")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._name = name
        self._category = category
        self.articles_list = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("Name must be a string")
        if not (2 <= len(new_name) <= 16):
            raise ValueError("Name length must be between 2 and 16 characters")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str):
            raise ValueError("Category must be a string")
        if len(new_category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = new_category

    def articles(self):
        return self.articles_list

    def contributors(self):
        return list(set([article.author for article in self.articles_list]))

    def article_titles(self):
        return [article.title for article in self.articles_list] if self.articles_list else None

    def contributing_authors(self):
        if not self.articles_list:
            return None
        authors_count = {}
        for article in self.articles_list:
            if article.author in authors_count:
                authors_count[article.author] += 1
            else:
                authors_count[article.author] = 1
        contributing_authors = [author for author, count in authors_count.items() if count > 2]
        return contributing_authors if contributing_authors else None
