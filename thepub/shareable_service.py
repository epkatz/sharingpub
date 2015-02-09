from thepub.models import UserProfile, Shareable


def save_shareable(user, url):
    user_profile = UserProfile.objects.get(user=user)
    u = Shareable(url=url, shared_by=user_profile)
    u.save()


def get_shareables_for_user(user):
    user_profile = UserProfile.objects.get(user=user)
    return Shareable.objects.filter(shared_by=user_profile)


