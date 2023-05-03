# blog.py 
import requests

class Blog:
		def posts(self):
				endereco = "https://jsonplaceholder.typicode.com/posts"
				response = resquest.get(endereco)
				return response.json()

		def post_by_user_id(self, userId:str):
				e = f"https://jsonplaceholder.typicode.com/post/{userid}"
				response = requests.get(e)
				return response.json()
