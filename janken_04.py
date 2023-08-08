import random

choices = ["グー", "チョキ", "パー"]
player_score = 0
computer_score = 0
rounds = 15
max_choices = 5
player_choices = {0: max_choices, 1: max_choices, 2: max_choices}
computer_choices = {0: max_choices, 1: max_choices, 2: max_choices}

print("じゃんけんゲームを開始します！")

for i in range(rounds):
    print(f"\n第{i+1}回戦")
    print(f"プレーヤーのポイント: {player_score}\tコンピューターのポイント: {computer_score}")

    print("\nあと何回出せるか:")
    print(f"グー: {player_choices[0]}\tチョキ: {player_choices[1]}\tパー: {player_choices[2]}")
    print(f"コンピューターの残り回数:")
    print(f"グー: {computer_choices[0]}\tチョキ: {computer_choices[1]}\tパー: {computer_choices[2]}")

    player_choice = input("あなたの手を選んでください（0:グー, 1:チョキ, 2:パー）: ")
    player_choice = int(player_choice)

    while player_choice < 0 or player_choice > 2 or player_choices[player_choice] == 0:
        player_choice = input("正しい手を選んでください（0:グー, 1:チョキ, 2:パー）: ")
        player_choice = int(player_choice)

    player_choices[player_choice] -= 1

    computer_choice = random.randint(0, 2)
    while computer_choices[computer_choice] == 0:
        computer_choice = random.randint(0, 2)

    computer_choices[computer_choice] -= 1

    print(f"あなたの手: {choices[player_choice]}\tコンピューターの手: {choices[computer_choice]}")

    if player_choice == computer_choice:
        print("引き分け！")
        player_score += 1
        computer_score += 1
    elif (player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 0):
        print("プレーヤーの勝ち！")
        player_score += 3
    else:
        print("コンピューターの勝ち！")
        computer_score += 3

print("\n対戦終了！")
print(f"最終結果 - プレーヤーのポイント: {player_score}\tコンピューターのポイント: {computer_score}")

if player_score > computer_score:
    print("プレーヤーの勝ち！")
elif player_score < computer_score:
    print("コンピューターの勝ち！")
else:
    print("引き分けです！")
