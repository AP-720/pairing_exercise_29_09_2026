def join_chat_participants(participants):
    if participants == []:
        return ""
    elif len(participants) <= 1:
        return participants[0]
    elif len(participants) <= 2:
        return participants[0] + " & " + participants[1]
    else:
        while True:
            count = 0
            results = ""
            for i in participants:
                results += participants[i] + ", "
                count += 1
                
            continue
                

#         return participants[0] + ", " + participants[1] + " & " + participants[2]