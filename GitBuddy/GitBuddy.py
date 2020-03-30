class git:
	def __init__(self,config):
		self.author_name = config['author_name']
		self.author_email = config['author_email']

	def init(self):
		"""make a bare repository"""
		pass

	def add(self,selector='.'):
		"""Add files in git"""
		pass

	def commit(self,message):
		"""Commit(Save) your work process with message identifier"""
		pass

	def push(self,remote_name,branch,mode='-u'):
		"""Push to the remote repository"""
		pass

	def pull(self,remote_name,branch):
		"""Pull from remote repository"""
		pass



class Github:
	def __init__(self,config):
		self.email = config['email']
		self.password = config['password']

	def create_repo(self):
		pass
	def rename_repo(self):
		pass
	def delete_repo(self):
		pass
	def make_release(self):
		pass