'''
	Config options for the stripe_payment app 
	Author: Muneeb Ali | http://muneeb.org
	License: MIT (see LICENSE)  
'''

import os

#-----------------------------------
# NOTE: It's not good practice to save keys in code files
# put the following lines in your ~/.bashrc instead
# export PUBLISHABLE_KEY=<your_stripe_publishable_key> 
# export SECRET_KEY=<your_stripe_secret_key>
#-----------------------------------
stripe_keys = {
	'secret_key': 'sk_test_vP2eMZcJwfYbtnjAqZlzgW8o009KOWZ6RT',
	'publishable_key': 'pk_test_QYHjBw7oe2FecykMKbGTQRZr00mliXkchY'
}

#-----------------------------------
# should be in cents
DEFAULT_CHARGE_AMOUNT = 525
DEFAULT_CHARGE_DESCRIPTION = "Flask Charge"

#-----------------------------------
DB_NAME = "stripe_customers"