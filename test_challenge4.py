import unittest
import challenge4
class test_challenge4(unittest.TestCase):
	def test_register(self):
		self.assertEqual(challenge4.register('kevin','koech','kevin','0102','0102','koechkevin59@yahoo.com'),True)
	def test_login(self):
		self.assertEqual(challenge4.login('kevin','0102'),'successful login')
		self.assertEqual(challenge4.login('kevin','0100'),'Invalid Credentials')
		self.assertEqual(challenge4.login('ken','0102'),'Invalid user, please register')
	def test_is_registered(self):
		self.assertEqual(challenge4.is_registered('kevin'),True)
		self.assertEqual(challenge4.is_registered('ken'),False)
	def test_is_loggedin(self):
		self.assertEqual(challenge4.is_loggedin('kevin'),True)
	def test_userInfo(self):
            self.assertEqual(challenge4.userInfo('kevin'),{'Username':'kevin','Name':'kevin  lastname','Email Address':'koechkevin59@yahoo.com','Password':'0102'})
            self.assertEqual(challenge4.userInfo('k'),{})
