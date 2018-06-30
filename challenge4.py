class challenge4(object):
	def __init__(self):
		self.details={}
		self.password={}
		self.posts=[]
		self.session={}
	def login(self,username,password):
		if username in self.details:
			if password==self.password[username]:
				self.session.update({username:self.details[username]})
				return('successful login')
			else:
				return('Invalid Credentials')
		else:
			return('Invalid user, please register')
	def logout(self,username):
		del self.session[username]
		return self.is_loggedin(username)
	def userInfo(self,username):
		
		if username in self.session:
			firstname=self.session[username][0]
			lastname=self.session[username][1]
			email=self.session[username][2]
			password=self.password[username]
			
			return {'Username':username,'Name':firstname+' '+lastname,'Email Address':email,'Password':password}
		else:
			return {}
	def register(self,firstname,lastname,username,password,confirmPassword,email):

		if self.passConfirm(password,confirmPassword):
			
			self.details.update({username:[firstname,lastname,email]})
			self.password.update({username:password})
			return username in self.details
		else:
			print('password should match')
			register(firstname,lastname,username,password,confirmPassword,email)
	def passConfirm(self,pass1,pass2):
		return pass1==pass2
	def comment(self,username,comment):
		if username in self.session:
			self.posts.append(comment)
			return self.posts
		else:
			return'please login!'
	def display_comments(self,username):
		if username in self.session:
			return self.posts
		else:
			return'please login'
	def is_registered(self,username):
		if username in self.details:
			return True
		else:
			return False
	def is_loggedin(self,username):
		if username in self.session:
			return True
		else:
			return False		
