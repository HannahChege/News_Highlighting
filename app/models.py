class Source:
    '''
    Article class to define Article Objects
    '''

    def __init__(self,id,name):
        self.id = id
        self.name = name
        
class Article:
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
        
        
        
