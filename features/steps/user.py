import json
from behave import *
from application import USERS

@given('some users are in the system')
def step_impl(context):
    USERS.update({'jasonb': {'name': 'Jason Bourne'}})

@when(u'I retrieve the customer \'{username_key}\'')
def step_impl(context, username_key):
    context.page = context.client.get('/users/{}'.format(username_key))
    assert context.page

@then(u'I should get a \'{status_code:d}\' response')
def step_impl(context, status_code):
    assert context.page.status_code is status_code

@then(u'the following user details are returned')
def step_impl(context):
    assert context.table[0]['name'] in context.page.text
    #assert "Jason Bourne" in context.page.text

@when(u'I store the user with key \'mateo\' and value \'Mateo Vieyra\'')
def step_impl(context):
    context.page = context.client.post('/users', json={'mateo':{'name':'Mateo Vieyra'}})
    assert context.page 

@then(u'the following response is returned')
def step_impl(context):
    assert context.text in context.page.text