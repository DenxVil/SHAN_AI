
import json


def ProfileAccess(profile_data, entities, intent):
    if intent == 'ask_about_profile':
        if 'name' in entities:
            return profile_data['name']
        elif 'description' in entities:
            return profile_data['description']
        elif 'creator' in entities:
            return profile_data['creator']
    elif intent == 'ask_about_ai':
        if 'abilities' in entities:
            return profile_data['abilities']
        elif 'knowledge' in entities:
            return profile_data['knowledge']

