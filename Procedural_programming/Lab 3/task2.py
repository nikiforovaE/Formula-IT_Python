def find_common_participants(participants_first, participants_second, delimiter=","):
    participants_first = set(participants_first.split(delimiter))
    participants_second = participants_second.split(delimiter)
    common_participants = list(participants_first.intersection(participants_second))
    common_participants.sort()
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, "|"))
