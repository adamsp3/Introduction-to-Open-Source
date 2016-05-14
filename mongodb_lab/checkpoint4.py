from pymongo import MongoClient 

client = MongoClient

if __name__ == '__main__':
	db = client.my_database
	posts = db.posts
	post = {"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"], "date": "08.18.15"}
	post_id = posts.insert_one(post)
	posts.find_one() 
	posts.find_one({"author": "Mike"})
	posts.find_one({"_id": post_id})


