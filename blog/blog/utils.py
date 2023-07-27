from .models import Post


def analyze_user_body(body):

    words_list = body.split()
    response = []

    for i in range(len(words_list)):
        if words_list[i] == 'hey':
            response.append('you are very expressive')
        else:
            continue


    return response
            


    
    