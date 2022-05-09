import os
from rest_framework import serializers
from django.core.exceptions import ValidationError

def correct_rank_validation(value):
    if not (1 <=value <=5 ):
        raise serializers.ValidationError('Invalid rank')

def validate_category(value):
    if not (value == 'Men' or value == 'Women'):
        raise serializers.ValidationError('Only Men and Women categories')

def validate_quantity(value):
    if (value >100):
        raise serializers.ValidationError('You can order maximum 100 products')


def validate_price(value):
    if (value >100000):
        raise serializers.ValidationError('Maximum price should be lower than 100000')


def validate_user(value):
    if (value=="qshop"):
        raise serializers.ValidationError('Please select the user, not admin')

def validate_owner(value):
    if (value != 1):
        raise serializers.ValidationError('Qshop is the admin!')




