import sqlite3
conexao = sqlite3.connect("voos.db")
cursor = conexao.cursor()


class Aeronaves:

    def cadastrar_novo(self, cod_aeronave, modelo_aeronave, assentos_disponiveis, limite_bagagem):
        cursor.execute(
            'INSERT INTO aeronaves (cod_aeronave, modelo_aeronave, assentos_disponiveis, limite_bagagem)'
            'VALUES(?, ?, ?, ?)',
            (cod_aeronave, modelo_aeronave, assentos_disponiveis, limite_bagagem))
        conexao.commit()

    def alterar_registro(self, opc, valor, cod_aeronave):
        opcs = {1: "cod_aeronave",
                2: "modelo_aeronave",
                3: "assentos_disponiveis",
                4: "limite_bagagem"}

        cursor.execute(f'UPDATE aeronaves SET {opcs[opc]}=? WHERE cod_aeronave=?', (valor, cod_aeronave))
        conexao.commit()

    def excluir_registro(self, cod_aeronave):
        cursor.execute('DELETE FROM aeronaves WHERE cod_aeronave=?', (cod_aeronave,))
        conexao.commit()


class Aeroportos:

    def cadastrar_novo(self, cod_aeroporto, nome_aeroporto, sigla_aeroporto, cidade_aeroporto, estado_aeroporto, pais_aeroporto, continente_aeroporto):
        cursor.execute(
            'INSERT INTO aeroportos (cod_aeroporto, nome_aeroporto, sigla_aeroporto, cidade_aeroporto, estado_aeroporto, pais_aeroporto, continente_aeroporto)'
            'VALUES(?, ?, ?, ?, ?, ?, ?)',
            (cod_aeroporto, nome_aeroporto, sigla_aeroporto, cidade_aeroporto, estado_aeroporto, pais_aeroporto, continente_aeroporto))
        conexao.commit()

    def alterar_registro(self, opc, valor, cod_aeroporto):
        opcs = {1: "cod_aeroporto",
                2: "nome_aeroporto",
                3: "sigla_aeroporto",
                4: "cidade_aeroporto",
                5: "estado_aeroporto",
                6: "pais_aeroporto",
                7: "continente_aeroporto"}

        cursor.execute(f'UPDATE aeroportos SET {opcs[opc]}=? WHERE cod_aeroporto=?', (valor, cod_aeroporto))
        conexao.commit()

    def excluir_registro(self, cod_aeroporto):
        cursor.execute('DELETE FROM aeroportos WHERE cod_aeroporto=?', (cod_aeroporto,))
        conexao.commit()


class Empresas_aereas:

    def cadastrar_novo(self, cod_empresa, nome_empresa, nacionalidade_empresa, sigla_empresa):
        cursor.execute(
            'INSERT INTO empresas_aereas (cod_empresa, nome_empresa, nacionalidade_empresa, sigla_empresa)'
            'VALUES(?, ?, ?, ?)',
            (cod_empresa, nome_empresa, nacionalidade_empresa, sigla_empresa))
        conexao.commit()

    def alterar_registro(self, opc, valor, cod_empresa):
        opcs = {1: "cod_empresa",
                2: "nome_empresa",
                3: "nacionalidade_empresa",
                4: "sigla_empresa"}

        cursor.execute(f'UPDATE a SET {opcs[opc]}=? WHERE cod_empresa=?', (valor, cod_empresa))
        conexao.commit()

    def excluir_registro(self, cod_empresa):
        cursor.execute('DELETE FROM empresas_aereas WHERE cod_empresa=?', (cod_empresa,))
        conexao.commit()


class Voos:

    def cadastrar_novo(self, cod_voo, data_saida, hora_saida, cod_aeroporto_decolagem, cod_aeroporto_destino, cod_empresa, n_passageiros, assentos_disponiveis, carga_carregada, cod_aeronave, data_chegada, hora_chegada, natureza_voo):
        cursor.execute(
            'INSERT INTO Voos (cod_voo, data_saida, hora_saida, cod_aeroporto_decolagem, cod_aeroporto_destino, cod_empresa, n_passageiros, assentos_disponiveis, carga_carregada, cod_aeronave, data_chegada, hora_chegada, natureza_voo)'
            'VALUES(?, ?, ?, ?)',
            (cod_voo, data_saida, hora_saida, cod_aeroporto_decolagem, cod_aeroporto_destino, cod_empresa, n_passageiros, assentos_disponiveis, carga_carregada, cod_aeronave, data_chegada, hora_chegada, natureza_voo))
        conexao.commit()

    def alterar_registro(self, opc, valor, cod_voo):
        opcs = {1: "cod_voo",
                2: "data_saida",
                3: "hora_saida",
                4: "cod_aeroporto_decolagem",
                5: "cod_aeroporto_destino",
                6: "cod_empresa",
                7: "n_passageiros",
                8: "assentos_disponiveis",
                9: "carga_carregada",
                10: "cod_aeronave",
                11: "data_chegada",
                12: "hora_chegada",
                13: "natureza_voo"}

        cursor.execute(f'UPDATE a SET {opcs[opc]}=? WHERE cod_voo=?', (valor, cod_voo))
        conexao.commit()

    def excluir_registro(self, cod_voo):
        cursor.execute('DELETE FROM Voos WHERE cod_voo=?', (cod_voo,))
        conexao.commit()


def filtro(opc, valor):
    if opc == 1:
        if type(valor) != tuple:
            print("ERRO por favor informe as datas em uma tupla")
        else:
            datas = []
            for i in valor:
                datas.append(data_certa(i))
            inicio = datas[0]
            fim = datas[1]
            for i in range(inicio, fim):
                try:
                    cursor.execute(f'SELECT n_passageiros, assentos_disponiveis, carga_carregada FROM Voos WHERE data_saida = ?', (i,))
                except:
                    pass
    else:
        opcs = {2: "cod_empresa", 3: "cod_aeroporto_decolagem" or "cod_aeroporto_destino "}
        cursor.execute(f'SELECT n_passageiros, assentos_disponiveis, carga_carregada FROM Voos WHERE {opcs[opc]} = ?', (valor,))
    for i in cursor.fetchall():
        print(f'Número de passageiros: {i[0]} - Assentos disponíveis: {i[1]} - Ocupação: {i[0]/i[1]} Carga carregada: {i[2]}')


def data_certa(data):
    data = data.replace("/", "").replace(".", "")
    return int(f"{data[4:]}{data[2:4]}{data[:2]}")


filtro(1, ("28/07/2022", "29/07/2022"))


cursor.close()
conexao.close()
