

def generate_response(profile_info):
    if isinstance(profile_info, list):
        response = ', '.join(profile_info)
    else:
        response = profile_info
    return f'The answer to your question is: {response}'

