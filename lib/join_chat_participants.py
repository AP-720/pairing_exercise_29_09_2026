def join_chat_participants(participants):
    if participants == []:
        return ""
    elif len(participants) <= 1:
        return participants[0]