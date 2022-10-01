# to make username as Email during login


from django.contrib.auth.models import User
class EmailAuthBackend(object):
	"""
	Email Authentication Backend

	Allows a user to sign in using an email/password pair rather than
	a username/password pair.
	"""
 
	def authenticate(self, username=None, password=None):
		""" Authenticate a user based on email address as the user name. """
		try:
			user = User.objects.get(email=username)
			if user.check_password(password):
				return user
		except User.DoesNotExist:
				return None
 
