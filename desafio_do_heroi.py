class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == 'mago':
            ataque = 'usou magia'
        elif self.tipo == 'guerreiro':
            ataque = 'usou espada'
        elif self.tipo == 'monge':
            ataque = 'usou artes marciais'
        elif self.tipo == 'ninja':
            ataque = 'usou shuriken'
        else:
            ataque = 'usou um ataque indefinido'

        mensagem = f"o {self.tipo} atacou usando {ataque}"
        return mensagem

# Exemplo de uso da classe
heroi1 = Heroi('Aragorn', 30, 'guerreiro')
print(heroi1.atacar())  # Saída: "o guerreiro atacou usando espada"

heroi2 = Heroi('Gandalf', 60, 'mago')
print(heroi2.atacar())  # Saída: "o mago atacou usando magia"
