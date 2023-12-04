import sqlite3

class SistemaCadastro:
    def __init__(self):
        self.conn = sqlite3.connect('pessoas.db')
        self.cursor = self.conn.cursor()
        self.criar_tabela_pessoa()

    def criar_tabela_pessoa(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Pessoa (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nome TEXT,
                                email TEXT,
                                telefone TEXT,
                                idade INTEGER
                            )''')
        self.conn.commit()

    def criar_pessoa(self, nome, email, telefone, idade):
        self.cursor.execute('''INSERT INTO Pessoa (nome, email, telefone, idade)
                            VALUES (?, ?, ?, ?)''', (nome, email, telefone, idade))
        self.conn.commit()

    def ler_todas_pessoas(self):
        self.cursor.execute('''SELECT * FROM Pessoa''')
        return self.cursor.fetchall()

    def atualizar_pessoa(self, id_pessoa, nome, email, telefone, idade):
        self.cursor.execute('''UPDATE Pessoa SET nome=?, email=?, telefone=?, idade=?
                            WHERE id=?''', (nome, email, telefone, idade, id_pessoa))
        self.conn.commit()

    def deletar_pessoa(self, id_pessoa):
        self.cursor.execute('''DELETE FROM Pessoa WHERE id=?''', (id_pessoa,))
        self.conn.commit()

    def fechar_conexao(self):
        self.conn.close()

def exibir_menu():
    print("### Sistema de Cadastro de Pessoas ###")
    print("1. Cadastrar Pessoa")
    print("2. Mostrar todas as Pessoas")
    print("3. Atualizar Pessoa")
    print("4. Deletar Pessoa")
    print("0. Sair")

def main():
    sistema = SistemaCadastro()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome da pessoa: ")
            email = input("Digite o e-mail da pessoa: ")
            telefone = input("Digite o telefone da pessoa: ")
            idade = int(input("Digite a idade da pessoa: "))

            sistema.criar_pessoa(nome, email, telefone, idade)
            print("Pessoa cadastrada com sucesso!")

        elif opcao == "2":
            pessoas = sistema.ler_todas_pessoas()
            if pessoas:
                for pessoa in pessoas:
                    print(pessoa)
            else:
                print("Não há pessoas cadastradas.")

        elif opcao == "3":
            id_pessoa = int(input("Digite o ID da pessoa que deseja atualizar: "))
            nome = input("Digite o novo nome da pessoa: ")
            email = input("Digite o novo e-mail da pessoa: ")
            telefone = input("Digite o novo telefone da pessoa: ")
            idade = int(input("Digite a nova idade da pessoa: "))

            sistema.atualizar_pessoa(id_pessoa, nome, email, telefone, idade)
            print("Pessoa atualizada com sucesso!")

        elif opcao == "4":
            id_pessoa = int(input("Digite o ID da pessoa que deseja deletar: "))
            sistema.deletar_pessoa(id_pessoa)
            print("Pessoa deletada com sucesso!")

        elif opcao == "0":
            print("Saindo do sistema...")
            sistema.fechar_conexao(),
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()