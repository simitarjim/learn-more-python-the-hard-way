from dictionary import Dictionary

# create a mapping of state to abbreviation
def test_set():
    states = Dictionary()
    states.set('Oregon', 'OR')
    states.set('Florida', 'FL')
    states.set('California', 'CA')
    states.set('New York', 'NY')
    states.set('Michigan', 'MI')
    assert states.get('Oregon') == 'OR'
    assert states.get('Florida') == 'FL'
    assert states.get('California') == 'CA'
    assert states.get('New York') == 'NY'
    assert states.get('Michigan') == 'MI'

    # create a basic set of states and some cities in them
    cities = Dictionary()
    cities.set('CA', 'San Fransico')
    cities.set('MI', 'Detriot')
    cities.set('FL', 'Jacksonville')

    # add some more cities
    cities.set('NY', 'New York')
    cities.set('OR', 'Portland')


# print out some cities
# print('-' * 10)
# print("NY State has: %s" % cities.get('NY'))
# print("OR State has: %s" % cities.get('OR'))

# # print some states
# print('-' * 10)
# print("Michigan's abbreviation is: %s" % states.get('Michigan'))
# print("Florida's abbreviation is: %s" % states.get('Florida'))

# # do it by using the state then cities dict
# print('-' * 10)
# print("Michigan has: %s" % cities.get(states.get('Michigan')))
# print("Florida has: %s" % cities.get(states.get('Florida')))

# # print every state abbreviation
# print('-' * 10)
# states.list()

# # print every city in state
# print('-' * 10)
# cities.list()

# print('-' * 10)
# state = states.get('Texas')

# if not state:
#     print("Sorry, no Texas.")

# # can you do this on one line?
# city = cities.get('TX', 'Does Not Exist')
# print("The city for the state 'TX' is: %s" % city)

# cities.delete('FL')
# city = cities.get('FL', 'Does Not Exist')
# print("FL should be gone: %r" % city)