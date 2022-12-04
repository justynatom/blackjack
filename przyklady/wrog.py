import random


class Player:

    def blast(self, enemy):
        print("gracz razi wroga \n")
        enemy.die()

    def pac(self, enemy):
        print("pac, pac")
        enemy.shout()

    def shoot(self, enemy):
        damage = random.randint(1, 10)
        print(damage)
        if damage >= 3:
            print("player win")
            enemy.die()
        else:
            print("enemy eat player")
            enemy.sleep()


class Alien:

    def die(self):
        print('Obcy z trudem łapie oddech, "To już koniec. Ale prawdziwie wielki koniec... \n',
              'Walczyliśmy do końca. Nie, to nie koniec. Larwy moje jednoczcie się! \n',
              'O tak one pomszczą mnie pewnego dnia... \n',
              'Żegnaj, okrutny Wszechświecie! Umieeeraaam"')

    def shout(self):
        print("ała")

    def sleep(self):
        print("mlask, mlask")

if __name__ == '__main__':
    print('************ Śmierć Obcego ************\n')
    hero = Player()
    invader = Alien()
    hero.pac(invader)
    hero.shoot(invader)
    # hero.blast(invader)

    input('\n\nAby zakończyć program, naciśnij klawisz Enter.')