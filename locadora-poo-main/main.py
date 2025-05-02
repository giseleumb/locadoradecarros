from modules import locadora
from utils import util

if __name__ == '__main__':
    app = locadora.App()
    
    userList, carList = app.loadLists()

    while(True):
        print('Tabela da Locadora')
        print('0 - Cadastrar veiculo')
        print('1 - Consultar disponibilidade de veículos')
        print('2 - Listar veículos por marca')
        print('3 - Listar veículos por modelo')
        print('4 - Listar veículos por ano')
        print('5 - Criar usuario')
        print('6 - alugar veiculo')
        print('7 - devolver veiculo')
        print('8 - Remover veículo')
        print('9 - Remover usuário')
        print('10 - Alterar nome de usuário')
        print('11 - Alterar veículo')




        try:
            resp = int(input('Digite sua escolha: '))

            match (resp):
                case 0:
                    car = app.cadastrar_veiculo()
                    carList.append(car)
                    util.pauseAndClear()
                case 1:
                    app.consultar_disponibilidade_de_veiculos(carList)
                    util.pauseAndClear()
                case 2:
                    app.listar_veiculos_por_marca(carList)
                    util.pauseAndClear()
                case 3:
                    app.listar_veiculos_por_modelo(carList)
                    util.pauseAndClear()
                case 4:
                    app.listar_veiculos_por_ano(carList)
                    util.pauseAndClear()
                case 5:
                    client = app.cadastrar_usuario()
                    userList.append(client)
                    util.pauseAndClear()
                case 6:
                    aluguel = app.alugar_veiculo(carList, userList)
                    
                    for user in userList:
                        if aluguel.user.id == user.id and user.nome == aluguel.user.nome:
                            user.atualizar_aluguel(aluguel)
                            
                    for car in carList:
                        if aluguel.car.placa == car.placa and aluguel.car.ano == car.ano:
                            car.set_estado()

                    util.pauseAndClear()
                case 7:
                    aluguel = app.devolver_veiculo(userList)
                    if aluguel:
                        for user in userList:
                            if aluguel.user.id == user.id and user.nome == aluguel.user.nome:
                                user.remover_aluguel(aluguel)
                        
                        for car in carList:
                            if aluguel.car.placa == car.placa and aluguel.car.ano == car.ano:
                                car.set_estado()
                                
                    util.pauseAndClear()

                case 8:
                    # Verifica se o carro existe antes de remover
                    placa = input("Informe a placa do veículo para remoção: ")
                    veiculo = next((car for car in carList if car.placa == placa), None)
                    if veiculo:
                        app.remover_veiculo(carList, placa)
                        util.pauseAndClear()
                    else:
                        print(f"Veículo com a placa {placa} não encontrado.")
                        util.pauseAndClear()

                case 9:
                    nome = input("Digite o nome do usuário para remoção: ")
                    app.remover_usuario(userList, nome)
                    util.pauseAndClear()
                
                case 10:
                    nome_antigo = input("Digite o nome atual do usuário: ")
                    novo_nome = input("Digite o novo nome do usuário: ")
                    app.alterar_usuario(userList, nome_antigo, novo_nome)
                    util.pauseAndClear()
                
                case 11:
                    app.alterar_veiculo(carList)
                    util.pauseAndClear()



                case _:
                    util.brokenProgram()
                    util.error()
                    break
        except:
            util.brokenProgram()
            util.error()
            break