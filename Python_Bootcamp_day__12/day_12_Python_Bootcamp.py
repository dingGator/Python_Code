print("*********Namespaces and Scope****")
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
    # Can't access this potion_strength outside of its scope
    # print(potion_strength)

# Global Scope
player_health = 10


def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()


print(player_health)

game()
print("*********block scope******")
game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]


def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


create_enemy()

print("********** prime number checker test*******8")

def is_prime(num):
    prime_flag = True
    if num == 0 or num == 1:
        prime_flag = False
    elif num > 1:
        for factor in range(2, num):
            if num % factor == 0:
                prime_flag = False
                break

    return prime_flag
is_prime(5)
print("******global vars****")
# Modifying Global Scope

enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

def increase_enemies(enemy):
    print(f"enemies inside function: {enemy}")
    return enemy + 1


enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")


