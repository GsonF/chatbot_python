import os

def start():
    def pross_perg(perguntas, nome):
        if perguntas == '1':
            print(f'{os.linesep}{nome},sou o Gilson. Atualmente estudo Engenharia de Software e tenho formação em Eletrônica pelo Instituto Federal de Alagoas. Fora dos estudos, adoro passar tempo com meus gatos e sou completamente viciado em café. Minha trajetória acadêmica reflete minha paixão pela tecnologia e meu entusiasmo em explorar as possibilidades na área de software.{os.linesep} ')
        elif perguntas == '2':
            print(f'{os.linesep}Bem,{nome}. Minha trajetória profissional inclui experiências como designer e social media, estágio em eletrônica e projetos diversos para meu portfólio, onde desenvolvi habilidades em programação. Também realizei trabalhos freelancer na área de software. Estou sempre em busca de novas oportunidades para continuar crescendo profissionalmente.{os.linesep} ')
        elif perguntas == '3':
            print(f'{os.linesep}Desde a escola, fiquei fascinado pela programação ao usar o Scratch. Mais tarde, na engine Godot, comecei a desenvolver jogos. Durante o ensino médio, decidi estudar C++ para aplicá-lo em projetos com Arduino, alinhando-me à minha escolha de carreira na área de eletrônica. Essas experiências iniciais foram fundamentais para minha paixão pela tecnologia e programação.{os.linesep} ')
        else:
            print("Digite apenas 1, 2 ou 3")

    # Apresenta chat
    print("Olá, bem-vindo ao meu portfólio!")
    
    # Solicita nome
    nome = input("Qual o seu nome? ")

    while True:
        # Opções 
        perguntas = input(f'O que gostaria de saber?{os.linesep}[1] - Quem é você?{os.linesep}[2] - Quais as suas experiências?{os.linesep}[3] - Como começou a programar? ')
        
        # Processa pergunta
        pross_perg(perguntas, nome)

if __name__ == '__main__':
    start()

