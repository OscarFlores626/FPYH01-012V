import os
import time
boleta=0
limpiezapantalla=("cls")
pikachuroll=4500
otakuroll=5000
pulporoll=5200
anguilaroll=4800
menu=1
menu2=0
menu3=0
cantidadroll1=0
cantidadroll2=0
cantidadroll3=0
cantidadroll4=0

while menu==1:
    print("1)Pikachu Roll: $4500 \n2)Otaku Roll: $5000 \n3)Pulpo Venenoso Roll: $5200 \n4)Anguila Electrica Roll: $4800")
    try:
        respuesta=int(input("Seleccione el roll que desea comprar ingresando el numero correspondiente: "))
        if respuesta== 1:
            cantidadroll1=int(input("Cuantos Rolls desea agregar?: "))
            boleta+= (cantidadroll1*pikachuroll)
            try:
                salida=int(input("Desea agregar otro roll? \n1)Si \n2)No \n"))
                if salida==1:
                    menu=1
                elif salida==2:
                    menu2=1
            except ValueError:
                print("Seleccione 1 para agregar mas rolls o 2 para salir")
        elif respuesta==2:
            cantidadroll2=int(input("Cuantos Rolls desea agregar?: "))
            boleta+= (cantidadroll2*otakuroll)
            try:
                salida=int(input("Desea agregar otro roll? \n1)Si \n2)No \n"))
                if salida==1:
                    menu=1
                elif salida==2:
                    menu2=1
            except ValueError:
                print("Seleccione 1 para agregar mas rolls o 2 para salir")
        elif respuesta==3:
            cantidadroll3=int(input("Cuantos Rolls desea agregar?: "))
            boleta+=(cantidadroll3*pulporoll)
            try:
                salida=int(input("Desea agregar otro roll? \n1)Si \n2)No \n"))
                if salida==1:
                    menu=1
                elif salida==2:
                    menu2=1
            except ValueError:
                print("Seleccione 1 para agregar mas rolls o 2 para salir")
        elif respuesta==4:
            cantidadroll4=int(input("Cuantos Rolls desea agregar?: "))
            boleta+=(cantidadroll4*anguilaroll)
            try:
                salida=int(input("Desea agregar otro roll? \n1)Si \n2)No \n"))
                if salida==1:
                    menu=1
                elif salida==2:
                    menu2=1
            except ValueError:
                    print("Seleccione 1 para agregar mas rolls o 2 para salir")
        else:
            print("Por favor ingrese una opcion valida")
            menu=1
    except ValueError:
            print("Ingrese una opcion valida porfavor")
    os.system(limpiezapantalla)
    while menu2==1:
        descuento=input("Ingrese su codigo de descuento: ")
        if descuento == "soyotaku":
            descuentofinal=(boleta*0.10)
            menu3=1
        else:
            salidamenu2=int (input("Su codigo no es valido desea ingresar nuevamente? \n1)Si \n2)No \n"))
            if salidamenu2==1:
                menu2=1
            elif salidamenu2==2:
                descuentofinal=0
                menu3=1
            else:
                print("Porfavor ingrese 1 para si y 2 para no")
        os.system(limpiezapantalla)
        while menu3==1:
            cantidadtotalroll=(cantidadroll1+cantidadroll2+cantidadroll3+cantidadroll4)
            print("TOTAL PRODUCTOS: ", cantidadtotalroll)
            print("Pikachu rolls: ", cantidadroll1)
            print("Otaku Roll: ", cantidadroll2)
            print("Pulpo Venenoso Roll: ", cantidadroll3)
            print("Anguila Electrica: ", cantidadroll4)
            print("************************************")
            print("Subtotal por pagar: $", boleta)
            print("Descuento por codigo: $", descuentofinal)
            print("TOTAL: $", (boleta-descuentofinal))
            salidafinal=int(input("Desea realizar otro pedido?: \n1)Si \n2)No \n"))
            if salidafinal==1:
                cantidadroll1=0
                cantidadroll2=0
                cantidadroll3=0
                cantidadroll4=0
                descuentofinal=0
                boleta=0
                menu2=0
                menu3=0
                menu=1
            elif salidafinal==2:
                menu=5
                menu2=5
                menu=5
                os.system(limpiezapantalla)
                print("Hasta luego vuelva pronto!")
                break
            else:
                    print("Porfavor ingrese 1 o 2")
