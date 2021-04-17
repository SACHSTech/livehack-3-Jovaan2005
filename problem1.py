win_loss_list = []
asked_total = 0
wins = 0
losses = 0
group = 0

print("Enter the wins and losses for your team: ")
while asked_total < 6:
    result = input("")
    if str.upper(result) == "W" or str.upper(result) == "L":
        win_loss_list.append(str.upper(result))
        asked_total = asked_total + 1

for i in win_loss_list:
    if i == "W":
        wins = wins + 1
    elif i == "L":
        losses = losses + 1

if wins >= 5:
    group = 1
elif wins >= 3:
    group = 2
elif wins >= 1:
    group = 3
else:
    group = "eliminated"

print(f"You are in the {group} group!")
    





