def run():
    '''Muestra enticades y personas a Notificar basado en el nivel de riesgo'''

    menu = '''
    BIENVENIDO!
    Lector del nivel de la calidad del agua en poblaciones apartadas.

    Seleccione el numero correspondiente a su eleccion:

       Nivel De Riesgo              Clasificacion IRCA(%)
    1. INVIABLE SANITARIAMENTE       80.1 - 100
    2. ALTO                          35.1 - 80
    3. MEDIO                         14.1 - 35
    4. BAJO                           5.1 - 14
    5. SIN RIESGO                       0 - 5

    Escribe el numero correspondiente a su eleccion: '''

    opcion = int(input(menu))

    if opcion == 1:
        print('\nNivel de riesgo Seleccionado, INVIABLE SANITARIAMENTE \nNotificar a las siguientes entidades:\n\nPersona prestadora\nCOVE\nAlcaldía\nGobernación\nSSPD\nMPS\nINS\nMAVDT\nContraloría General\nProcuraduría General')
    elif opcion == 2:
        print('\nNivel de riesgo Seleccionado, ALTO \nNotificar a las siguientes entidades:\n\nPersona prestadora\nCOVE\nAlcaldía\nGobernación\nSSPD')
    elif opcion == 3:
        print('\nNivel de riesgo Seleccionado, MEDIO \nNotificar a las siguientes entidades:\n\nPersona prestadora\nCOVE\nAlcaldía\nGobernación')
    elif opcion == 4:
        print('\nNivel de riesgo Seleccionado, BAJO \nNotificar a las siguientes entidades:\n\nPersona prestadora\nCOVE')
    elif opcion == 5:
        print('\nNivel de riesgo Seleccionado, SIN RIESGO\n\nContinuar el control y la vigilancia')
    else:
        print('\nNo es un nivel de riesgo catalogado')


if __name__ == '__main__':
    run()
    