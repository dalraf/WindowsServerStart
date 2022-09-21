from instalacao import (
    install_chocolatey,
    install_google_chrome,
    install_firefox,
    install_openssh,
)

menu = [
    ["Chocolatey", install_chocolatey],
    ["Google Chrome", install_google_chrome],
    ["Firefox", install_firefox],
    ["Openssh", install_openssh],
]

while (True):
    for indice, value in enumerate(menu):
        print(indice, '- Instalar ', value[0],)
    print('99 - Instalar tudo')

    status = input("Digite a opção desejada:")

    if status == '99':
        for i in menu:
            i[1]()
    else:
        menu[int(status)][1]()
