from colorama import init, Fore, Back, Style
init()

print(f"{Fore.RED}=== Calculadora de Descuentos Inteligente ===")
while True:
    producto = input(f"{Fore.BLUE}Ingresa el nombre del producto: ")
    while True:
        precio_original = input(f"{Fore.GREEN}Ingresa el precio original del producto: ")
        precio_originalf=float(precio_original) #CASTING
        if (precio_originalf < 1): 
            print(f"Error: Debes ingresar un número valido")
            continue
        break
    while True: 
        porcentaje_descuento = input(f"{Fore.RED}Ingresa el porcentaje de descuento (sin el símbolo %): ")
        porcentaje_df=float(porcentaje_descuento) #CASTING
        if (porcentaje_df < 1): 
            print(f"Error: Debes ingresar un número valido")
            continue
        break
    monto_descuento = (porcentaje_df / 100) * precio_originalf
    precio_final = precio_originalf - monto_descuento

    print("\n=== Resumen de tu compra ===")
    print(f"{Fore.MAGENTA}Producto: {producto}")
    print(f"{Fore.MAGENTA}Precio original: ${precio_originalf:}")
    print(f"{Fore.MAGENTA}Descuento aplicado: {porcentaje_df:}%")
    print(f"{Fore.MAGENTA}Monto del descuento: ${monto_descuento:}")
    print(f"{Fore.RED}Precio final: ${precio_final:}")

    repetir = input(f"\n {Fore.CYAN}¿Quieres calcular otro descuento? (s/n): ").strip().lower()
    if repetir != 's':
        print("Gracias por usar la calculadora de descuentos. ¡Vuelva pronto!")
        break
