class Article:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,id,name,category):
        self.id = id
        self.name = name
        self.category = category
class Source:
    '''
   Source class to define Source Objects
    '''

    def __init__(self,source,author,title,description,url,urlToImage,publishedAt):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        
        
        
