productos = {'C-123': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
        'C-111': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
        'C-234': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
        'C-456': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
        'C-1222': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
        'C-477': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
        'C-334': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
        'C-2906': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'C-123': [387990,10], 
        'C-111': [327990,4], 
        'C-234': [424990,1],
        'C-456': [664990,21], 
        'C-477': [290890,32], 
        'C-334': [444990,7],
        'C-1222': [749990,2], 
        'C-2906': [349990,1]}

def stock_marca(lst_productos:dict,lst_stock:dict,marca_buscada:str)->int:
        for codigo, dato in lst_stock.items():
                if marca_buscada==lst_productos[codigo][0]:
                        print("walala")
                

def busqueda_precios(lst_productos:dict,lst_stock:dict,p_min:int,p_max:int)->None:
        for codigo, info in lst_stock.items():
                precio=info[0]
                stock=info[1]
                marca=lst_productos[codigo][0]
                if precio>=p_min and precio <=p_max and stock>0:
                        print(f"el producto {codigo}-{marca} esta en el rango de precio")

def actualizar_precios(lst_stock:dict,codigo:str,nuevo_precio:int)->bool:
        if codigo in lst_stock:
                lst_stock[codigo][0]=nuevo_precio
                return True
        return False

while True:
        print("1.Consultar stock de marca especifica")
        print("2.Buscar productos por rango de precio")
        print("3.Actualizar precio de un producto")
        print("4.Salir del progra")
        while True:
                try:
                        opcion=int(input("elija una opcion: "))
                except ValueError:
                        print("ingrese un valor numerico")
                else:
                        break
        if opcion==1:
                marca_buscada=input("que maraca quiere buscar: ").lower()
                
                if marca_buscada in productos:
                        print(stock_marca(lst_stock=[1]))
                        
        elif opcion==2:
                try: 
                        p_min=int(input("ingrese el precio minimo: "))
                        p_max=int(input("ingrese el precio maximo: "))
                except ValueError:
                        print("ingrese solo valores numericos, sin coma")
                if busqueda_precios(productos, stock,p_min,p_max):
                        print("se a encontrado el producto")
                
        elif opcion==3:
                codigo=input("ingrese el codigo del producto para cambiar su precio: ").strip()
                try:
                        nuevo_precio=int(input("ingrese el nuevo precio del producto: "))
                except ValueError:
                        print("ingrese solo valores numericos, sin coma")
                if actualizar_precios==True:
                        print("se a cambiado correctamente el precio")
                else:
                        print("no se a podido cambiar el precio")
        elif opcion==4:
                print("cerrando programa")
                
                break
        else:
                print("ingrese un valor del 1 al 4. ")