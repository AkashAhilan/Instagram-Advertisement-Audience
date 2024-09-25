import instaloader

def get_followers(username, L):
    # Fetch the profile for the given username
    profile = instaloader.Profile.from_username(L.context, username)
    
    # Fetch and store all the followers for that profile
    followers = set(follower.username for follower in profile.get_followers())
    
    return followers

def common_followers(account_list, L):
    if not account_list:  # If the list is empty, return an empty set
        return set()

    # Get the followers for the first account
    common = get_followers(account_list[0], L)

    # Iterate through the other accounts and intersect their followers with the common set
    for account in account_list[1:]:
        common &= get_followers(account, L)  # Keep only followers that are common to all accounts

    return common

if __name__ == "__main__":
    L = instaloader.Instaloader()

    # Login with your Instagram credentials
    username = 'your_instagram_username'
    password = 'your_instagram_password'
    L.login(username, password)

    # List of Instagram accounts to check
    accounts = ['account1', 'account2', 'account3']  # Replace with real accounts

    # Get the common followers
    common = common_followers(accounts, L)

    if common:
        print(f"Common followers: {common}")
    else:
        print("No common followers found.")
