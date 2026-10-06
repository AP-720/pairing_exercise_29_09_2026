def join_chat_participants(participants):
    if participants == []:
        return ""
    elif len(participants) <= 1:
        return participants[0]
    elif len(participants) <= 2:
        return participants[0] + " & " + participants[1]
    else:
        return participants[0] + ", " + participants[1] + " & " + participants[2]