import os

# Lista de restaurantes cadastrados, cada um representado por um dicionário
restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False}, 
    {'nome': 'Pizza Superma', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}
]

def exibir_nome_do_programa():
    """
    Exibe o nome do sistema de gerenciamento de restaurantes.

    Esta função imprime o nome "Sabor Express" com uma quebra de linha,
    funcionando como título principal da aplicação.
    """
    print('Sabor Express\n')


def exibir_opcoes():
    """
    Exibe o menu principal de opções disponíveis ao usuário.

    As opções incluem: cadastrar, listar, alternar estado de restaurantes e sair do programa.
    """
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair \n')


def exibir_subtitulo(texto):
    """
    Exibe um subtítulo formatado com linhas acima e abaixo.

    Args:
        texto (str): O texto a ser exibido como subtítulo.

    A função também limpa o terminal antes da exibição.
    """
    os.system('clear')
    linha = '=' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()


def finalizar_app():
    """
    Finaliza o aplicativo.

    Exibe uma mensagem informando o encerramento do programa.
    """
    exibir_subtitulo('Finalizando o app')


def voltar_ao_menu_principal():
    """
    Pausa o programa até o usuário pressionar uma tecla.

    Após a interação, retorna para o menu principal do sistema.
    """
    input('\nDigite uma tecla para voltar ao menu principal')
    main()


def opcao_invalida():
    """
    Informa ao usuário que a opção inserida é inválida.

    Esta função é chamada quando a entrada não corresponde às opções do menu.
    """
    print('Opção Inválida!')


def cadastrar_novo_restaurante():
    """
    Cadastra um novo restaurante na lista.

    Solicita ao usuário o nome e a categoria do restaurante,
    e adiciona um novo dicionário à lista global `restaurantes` com status desativado por padrão.

    Inputs:
        - Nome do restaurante (str)
        - Categoria do restaurante (str)

    A função exibe uma mensagem de sucesso ao final e retorna ao menu principal.
    """
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input('Digite a categoria do restaurante: ')
    restaurantes.append({'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False})

    print(f'\nO restaurante "{nome_do_restaurante}" foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()


def listar_restaurantes():
    """
    Lista todos os restaurantes cadastrados no sistema.

    Exibe os dados em uma tabela com colunas: Nome, Categoria e Status (ativo/desativado).
    Após a exibição, retorna ao menu principal.
    """
    exibir_subtitulo('Listando restaurantes')

    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status\n")
    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        status = 'ativo' if restaurante['ativo'] else 'desativado'
        print(f"- {nome.ljust(20)} | {categoria.ljust(20)} | {status}")

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    """
    Alterna o estado (ativo/desativado) de um restaurante pelo nome.

    Solicita ao usuário o nome de um restaurante existente e inverte o seu estado.
    Caso o restaurante não seja encontrado, uma mensagem de erro é exibida.
    """
    exibir_subtitulo('Alterando estado do restaurante')
    nome_procurado = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_procurado == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            status = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'\nO restaurante "{nome_procurado}" foi {status} com sucesso.')
            break

    if not restaurante_encontrado:
        print('\nO restaurante não foi encontrado.')

    voltar_ao_menu_principal()


def escolher_opcoes():
    """
    Captura a opção inserida pelo usuário e chama a função correspondente.

    Valida a entrada e redireciona para:
        1 - Cadastro de restaurante
        2 - Listagem de restaurantes
        3 - Alternar estado de restaurante
        4 - Encerrar aplicativo

    Em caso de erro ou valor inválido, informa o usuário.
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()


def main():
    """
    Função principal da aplicação.

    Limpa a tela, exibe o nome do sistema, mostra o menu de opções e inicia o fluxo do programa.
    """
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()


if __name__ == '__main__':
    main()
