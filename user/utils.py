def find_user_byid_followers(content, user):
    result=[]
    for i in content['followers']:
        x = user.objects.filter(id=i['from_user_id']).values('username').first()

        result.append(x)
    return result


def find_user_byid_followering(content, user):
    result=[]
    for i in content['followings']:
        x = user.objects.filter(id=i['to_user_id']).values('username').first()

        result.append(x)
    return result
