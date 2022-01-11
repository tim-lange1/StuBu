from flask import Flask, request


def multiply(query_result):
    num1 = int(query_result.get('parameters').get('number'))
    num2 = int(query_result.get('parameters').get('number1'))
    product = str(num1 * num2)
    print('here num1 = {0}'.format(num1))
    print('here num2 = {0}'.format(num2))
    fulfillmentText = 'The product of the two numbers is '+product
    return fulfillmentText

