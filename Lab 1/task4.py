users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
unique_users = set(users)
visits = {
    "Общее количество": len(users),
    "Уникальные посещения": len(unique_users)
}

print(visits)
