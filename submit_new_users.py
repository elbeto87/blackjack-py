class User:

    def __init__(self):
        self.name = input("Ingrese su nombre: ").capitalize()
        self.balance = int(input("Con cuanto dinero va a ingresar?: "))

    def __str__(self):
        return "Nombre del jugador: ",self.name,"\nDinero disponible en cuenta: ",self.balance

    def more_money(self):
        add_money = int(input("Cuanto dinero más vas a sumar a tu balance? "))
        self.balance += add_money
        print("Su nuevo balance es de ${}".format(self.balance))