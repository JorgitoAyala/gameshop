# importing files
from utils.console import drawUI, drawTables, clear, lazyMessage, runFile
from api.general import searchByAttribute, getQuantity, addData, readAllData, updateData
from utils.security import decrypt
from utils.validation import validationBankingCard
from utils.conversion import lineStringWrap, fromStringToList

# Dashboard del usuario OPCION 1: Juegos disponibles
def availableGames(type_of_user: str, user_id: str):
  clear()

  print()
  print("*"*82)
  print(drawUI(1, ""))
  print(drawUI(1, f" Juegos disponibles 😆 !! "))
  print(drawUI(1, ""))
  print(drawUI(3, "¿Que deseas hacer? 🤔"))
  print(drawUI(1, ""))
  print(drawUI(3, "A) Ver todos los juegos 🎮"))
  print(drawUI(3, "B) Comprar un juego 😄"))
  print(drawUI(3, "C) Volver al dashboard principal 😮"))
  print(drawUI(1, ""))
  print("*"*82)
  print()

  opc = input("|| => 😆 Selecciona una opción: ").upper()
  print()

  match opc:
    case "A": return viewAllGames(type_of_user, user_id)
    case "B": return buyOneGame(type_of_user, user_id)
    case "C":
      from app.dashboard import userDashboard
      return userDashboard(type_of_user, user_id)
    case _: 
      print("No válido, seleccione una opción nuevamente 🤭 !", end="\n\n")
      lazyMessage("|| Reiniciando en ", 3)
      return availableGames(type_of_user, user_id)

# Ver todos los productos disponibles en el archivo csv
def viewAllGames(type_of_user: str, user_id: str):
  clear()

  products = readAllData("./data/producto.csv")
  loops = len(products)

  print()
  print("*"*82)
  print(drawUI(1, ""))
  print(drawUI(1, f" Juegos de Gameshop 🤓 !! "))
  print(drawUI(1, ""))
  print("*"*82)
  print()
  
  for i in range(0, loops, 2):
    p1 = products[i]
    p2 = None if(i == loops - 1 and loops % 2 != 0) else products[i+1]

    print("*"*40 + (("  " + "*"*40) if p2 else ""))
    print(drawTables(1, {"p1": "", "p2": "" if p2 else None }))
    print(drawTables(1, {
      "p1": f" {p1.get('name')} ", 
      "p2": f" {p2.get('name')} " if p2 else None
      }))
    print(drawTables(1, {"p1": "", "p2": "" if p2 else None }))
    print(drawTables(3, {
      "p1": f"Hecho en: {p1.get('filetype')}",
      "p2": f"Hecho en: {p2.get('filetype')}" if p2 else None
      }))
    print(drawTables(1, {"p1": "", "p2": "" if p2 else None }))
    print(drawTables(3, {
      "p1": f"🆔 Id: {p1.get('id')}", 
      "p2": f"🆔 Id: {p2.get('id')}" if p2 else None
      }))
    print(drawTables(3, {
      "p1": f"👻 Categoría: {p1.get('category')}", 
      "p2": f"👻 Categoría: {p2.get('category')}" if p2 else None
      }))
    print(drawTables(3, {
      "p1": f"💰 Precio: S/. {p1.get('price')}.00",
      "p2": f"💰 Precio: S/. {p2.get('price')}.00" if p2 else None
      }))
    print(drawTables(3, {
      "p1": f"😎 Meta: {p1.get('goal')}", 
      "p2": f"😎 Meta: {p2.get('goal')}" if p2 else None
      }))
    print(drawTables(3, {
      "p1": f"🤑 Vendidos: {p1.get('selled')}",
      "p2": f"🤑 Vendidos: {p2.get('selled')}" if p2 else None
      }))
    print(drawTables(1, {"p1": "", "p2": "" if p2 else None }))
    print("*"*40 + (("  " + "*"*40) if p2 else ""))
    print()
  
  opc = input("|| => 😮 Tipea 'A' para regresar: ").upper()
  print()

  match opc:
    case "A": return availableGames(type_of_user, user_id)
    case _: 
      print("No válido, tipéalo nuevamente 🤭 !", end="\n\n")
      lazyMessage("|| Reiniciando en ", 3)
      return availableGames(type_of_user, user_id)

# Para comprar un juego
def buyOneGame(type_of_user: str, user_id: str):

  print("*"*82)
  print(drawUI(1, ""))
  print(drawUI(1, f" Vamos a comprar tu juego favorito 🤑 ! "))
  print(drawUI(1, ""))
  # Hacer la verificación si el producto existe
  game_id = input("|| => 🎮 Indica el ID o código del producto: ")
  product = searchByAttribute("id", game_id.upper(), "./data/producto.csv")
  print(drawUI(1, ""))
  print("*"*82)
  print()

  if(product is None):
    return errorBuyFound(
      type_of_user,
      "El código no existe 😱 .. debes escoger otro juego 😮 !",
      user_id,
    )

  print("|| => Este es el juego que encontramos 😆 : ")

  print()
  print("*"*40)
  print(drawTables(1, { "p1": "", "p2": None }))
  print(drawTables(1, { "p1": f" {product.get('name')} ", "p2": None }))
  print(drawTables(1, { "p1": "", "p2": None }))
  print(drawTables(3, { "p1": f"Hecho en: {product.get('filetype')}", "p2": None }))
  print(drawTables(1, { "p1": "", "p2": None }))
  print(drawTables(3, { "p1": f"🆔 Id: {product.get('id')}", "p2": None }))
  print(drawTables(3, { "p1": f"👻 Categoría: {product.get('category')}", "p2": None }))
  print(drawTables(3, { "p1": f"💰 Precio: S/. {product.get('price')}.00", "p2": None }))
  print(drawTables(3, { "p1": f"😎 Meta: {product.get('goal')}", "p2": None }))
  print(drawTables(3, { "p1": f"🤑 Vendidos: {product.get('selled')}", "p2": None }))
  print(drawTables(1, { "p1": "", "p2": None }))
  print("*"*40)
  print()

  verification = input("|| => ¿Es correcto el juego escogido 😮 ? (S/N) ").upper()
  print()

  if(verification == "S"):
    if(clientDashPassAuth(user_id)):
      return paymentCardAuth(type_of_user, user_id, product)
    else:
      print(f"No puede pagar si la contraseña no es correcta 🤬 !")
      print(f"Intente el proceso nuevamente 😐 ...", end="\n\n")
      lazyMessage("|| Reiniciando en ", 3)
      print()
      return availableGames(type_of_user, user_id)
  elif (verification == "N"):
    print("Tienes que escoger otro producto nuevamente 😮 !", end="\n\n")
    lazyMessage("|| Reiniciando en ", 3)
    print()
    return buyOneGame(type_of_user, user_id)
  else:
    print("No válido, seleccione una opción nuevamente 🤭 !", end="\n\n")
    lazyMessage("|| Reiniciando en ", 3)
    print()
    return buyOneGame(type_of_user, user_id)

# Pasarela de pagos con tarjeta de credito
def paymentCardAuth(type_of_user: str, user_id: str, product: dict):
  print()
  print("*"*82)
  print(drawUI(1, ""))
  print(drawUI(1, f" Bienvenido a la pasarela de Pagos 🤑 ! "))
  print(drawUI(1, ""))
  print(drawUI(3, "¿Con qué tarjeta bancaria deseas pagar? 🤔"))
  print(drawUI(1, ""))
  print(drawUI(3, "A) Visa 💳"))
  print(drawUI(3, "B) MasterCard 💳"))
  print(drawUI(3, "C) Discover 💳"))
  print(drawUI(3, "D) American Express 💳"))
  print(drawUI(3, "E) Diners Club 💳"))
  print(drawUI(3, "F) JCB 💳"))
  print(drawUI(3, "G) Volver al dashboard principal 😮"))

  print(drawUI(1, ""))
  opc = input("|| => 😆 Selecciona una opción: ").upper()

  print(drawUI(1, ""))
  print(drawUI(3, "¿Cúal es el número de la tarjeta de crédito 🧐 ?"))
  card_number = input("|| => ")

  print(drawUI(1, ""))
  print(drawUI(3, "¿Cúal es la fecha de vencimiento de la tarjeta (MM/AA) 📆 ?"))
  date_number = input("|| => ")
  validPayment = validationBankingCard(date_number, "date_number")
  if(not(validPayment.get("v"))): 
    return errorCardFound(type_of_user, validPayment.get("m"), user_id)
  
  print(drawUI(1, ""))
  print(drawUI(3, "¿Cúal es la clave de seguridad de la tarjeta 🔐 ?"))
  cvv2_number = input("|| => ")
  validPayment = validationBankingCard(cvv2_number, "cvv2_number")
  if(not(validPayment.get("v"))): 
    return errorCardFound(type_of_user, validPayment.get("m"), user_id)
  
  print(drawUI(1, ""))
  print("*"*82)
  print()

  match opc:
    case "A": 
      validPayment = validationBankingCard(card_number, "visa")
      if(not(validPayment.get("v"))): 
        return errorCardFound(type_of_user, validPayment.get("m"), user_id)
    case "B": 
      validPayment = validationBankingCard(card_number, "mastercard")
      if(not(validPayment.get("v"))): 
        return errorCardFound(type_of_user, validPayment.get("m"), user_id)
    case "C": 
      validPayment = validationBankingCard(card_number, "discover")
      if(not(validPayment.get("v"))): 
        return errorCardFound(type_of_user, validPayment.get("m"), user_id)
    case "D": 
      validPayment = validationBankingCard(card_number, "american_express")
      if(not(validPayment.get("v"))): 
        return errorCardFound(type_of_user, validPayment.get("m"), user_id)
    case "E": 
      validPayment = validationBankingCard(card_number, "diners_club")
      if(not(validPayment.get("v"))): 
        return errorCardFound(type_of_user, validPayment.get("m"), user_id)
    case "F":
      validPayment = validationBankingCard(card_number, "jcb")
      if(not(validPayment.get("v"))): 
        return errorCardFound(type_of_user, validPayment.get("m"), user_id)
    case "G": return availableGames(type_of_user, user_id)
    case _: 
      print("No válido, seleccione una opción nuevamente 🤭 !", end="\n\n")
      lazyMessage("|| Reiniciando en ", 3)
      return availableGames(type_of_user, user_id)
    
  if(validPayment):

    # Actualizar la cantidad de juegos del cliente
    client_info = searchByAttribute("id", user_id, "./data/cliente.csv")
    client_games = fromStringToList(client_info.get("games")) # [""] ó ["P1", "P2"]

    # Tengo que verificar si el elemento existe en la lista
    if product.get('id') in client_games:
      print("|| => Lamentablemente, no puede comprar un juego que ya tiene. ")
      print("||    Se cancela el proceso de pago 😅 ! ", end="\n\n")
      lazyMessage("|| Reiniciando en ", 3)
      print()
      return availableGames(type_of_user, user_id)

    # Una vez verificado, realizar la actualización
    if (client_games[0] == ""):
      gamesUpdated = f"[{product.get('id')}]" # [P1]
    else:
      originalString = client_info.get("games") # [P1-P2]
      gamesUpdated = originalString[:-1] + f"-{product.get('id')}" + originalString[-1:]
    
    updateData(user_id, "games", gamesUpdated, "./data/cliente.csv")

    # Aumentar la venta del producto
    product_quantity = int(product.get("selled")) + 1
    updateData(product.get("id"), "selled", str(product_quantity), "./data/producto.csv")

    print()
    print("*"*82)
    print(drawUI(1, ""))
    print(drawUI(1, f" Felicitaciones!, adquirió {product.get('name')} "))
    print(drawUI(1, ""))
    print("*"*82)
    print()

    print(f"¡Felicidades el juego fue comprado exitósamente 🎉🎉🎉 !", end="\n\n")
    lazyMessage("|| Reiniciando en ", 7)
    print()
    return availableGames(type_of_user, user_id)

# Verificar pidiendo la contraseña para realizar cambios
def clientDashPassAuth(user_id: str):
  result = searchByAttribute("id", user_id, "./data/cliente.csv")

  print()
  print("*"*82)
  print(drawUI(1, ""))
  print(drawUI(1, f" Antes de pagar, verifica tu contraseña: 🤫 "))
  print(drawUI(1, ""))
  my_password = input(f"|| => 🔒 Ingresa tu contraseña: ")
  print(drawUI(1, ""))
  print("*"*82)
  print()

  return decrypt(result.get("password")) == my_password

# En caso haya un error
def errorBuyFound(type_of_user: str, type_of_error: str, user_id: str):

  print("*"*82)
  print(drawUI(1, ""))
  print(drawUI(1, " Hay un error 🤬 !! "))
  print(drawUI(1, ""))
  print(f"|| => {type_of_error} ")
  print(drawUI(1, ""))
  print(drawUI(2, "A) Intentar nuevamente"))
  print(drawUI(2, "B) Regresar al dashboard principal"))
  print(drawUI(1, ""))
  print("*"*82)
  print()

  opc = input("|| => 😆 Selecciona una opción: ").upper()
  print()

  match opc:
    case "A": return buyOneGame(type_of_user, user_id)
    case "B": return availableGames(type_of_user, user_id)
    case _: 
      print("No válido, seleccione una opción nuevamente 🤭 !", end="\n\n")
      return errorBuyFound(type_of_user, type_of_error, user_id)

def errorCardFound(type_of_user: str, type_of_error: str, user_id: str):
  print()
  print("*"*82)
  print(drawUI(1, ""))
  print(drawUI(1, " Hay un error 🤬 !! "))
  print(drawUI(1, ""))
  print(lineStringWrap(f"|| => Mensaje: '{type_of_error}' 😯", 50))
  print(drawUI(1, ""))
  print(drawUI(2, "A) Intentar nuevamente"))
  print(drawUI(2, "B) Regresar al inicio de sesión"))
  print(drawUI(1, ""))
  print("*"*82)
  print()

  opc = input("|| => 😆 Selecciona una opción: ").upper()
  print()

  match opc:
    case "A": return buyOneGame(type_of_user, user_id)
    case "B": return availableGames(type_of_user, user_id)
    case _: 
      print("No válido, seleccione una opción nuevamente 🤭 !", end="\n\n")
      return errorCardFound(type_of_user, type_of_error, user_id)

# Dashboard del usuario OPCION 2: Mis Juegos comprados
def myGames(type_of_user: str, user_id: str):
  clear()

  client_info = searchByAttribute("id", user_id, "./data/cliente.csv")
  client_games = fromStringToList(client_info.get("games"))

  if (client_games[0] == ""):
    print()
    print("*"*82)
    print(drawUI(1, ""))
    print(drawUI(1, f" No tienes ningún juego hasta el momento 😢 !! "))
    print(drawUI(1, ""))
    print(drawUI(3, "Te sugerimos comprar uno 😁 , ¿Que deseas hacer?"))
    print(drawUI(1, ""))
    print(drawUI(3, "A) Comprar un juego 😄"))
    print(drawUI(3, "B) Volver al dashboard principal 😮"))
    print(drawUI(1, ""))
    print("*"*82)
    print()

    opc = input("|| => 😆 Selecciona una opción: ").upper()
    print()

    match opc:
      case "A": return availableGames(type_of_user, user_id)
      case "B": 
        from app.dashboard import userDashboard
        return userDashboard(type_of_user, user_id)
      case _: 
        print("No válido, seleccione una opción nuevamente 🤭 !", end="\n\n")
        lazyMessage("|| Reiniciando en ", 3)
        return availableGames(type_of_user, user_id)
    
  else:
    # Mostrar la cantidad de juegos que tiene el cliente
    print()
    print("*"*82)
    print(drawUI(1, ""))
    print(drawUI(1, f" Mis Juegos de Gameshop 🤓 !! "))
    print(drawUI(1, ""))
    print("*"*82)
    print()

    # ["P1", "P2", "P3"]
    loops = len(client_games)

    for i in range(0, loops, 2):

      p1 = searchByAttribute("id", client_games[i], "./data/producto.csv")

      if (i == loops - 1 and loops % 2 != 0):
        p2 = None
      else:
        p2 = searchByAttribute("id", client_games[i+1], "./data/producto.csv")

      print("*"*40 + (("  " + "*"*40) if p2 else ""))
      print(drawTables(1, {"p1": "", "p2": "" if p2 else None }))
      print(drawTables(1, {
        "p1": f" {p1.get('name')} ", 
        "p2": f" {p2.get('name')} " if p2 else None
        }))
      print(drawTables(1, {"p1": "", "p2": "" if p2 else None }))
      print(drawTables(3, {
        "p1": f"Hecho en: {p1.get('filetype')}",
        "p2": f"Hecho en: {p2.get('filetype')}" if p2 else None
        }))
      print(drawTables(1, {"p1": "", "p2": "" if p2 else None }))
      print(drawTables(3, {
        "p1": f"🆔 Id: {p1.get('id')}", 
        "p2": f"🆔 Id: {p2.get('id')}" if p2 else None
        }))
      print(drawTables(3, {
        "p1": f"👻 Categoría: {p1.get('category')}", 
        "p2": f"👻 Categoría: {p2.get('category')}" if p2 else None
        }))
      print(drawTables(3, {
        "p1": f"💰 Precio: S/. {p1.get('price')}.00",
        "p2": f"💰 Precio: S/. {p2.get('price')}.00" if p2 else None
        }))
      print(drawTables(3, {
        "p1": f"😎 Meta: {p1.get('goal')}", 
        "p2": f"😎 Meta: {p2.get('goal')}" if p2 else None
        }))
      print(drawTables(3, {
        "p1": f"🤑 Vendidos: {p1.get('selled')}",
        "p2": f"🤑 Vendidos: {p2.get('selled')}" if p2 else None
        }))
      print(drawTables(1, {"p1": "", "p2": "" if p2 else None }))
      print("*"*40 + (("  " + "*"*40) if p2 else ""))
      print()
    
    print("*"*82)
    print(drawUI(1, ""))
    print(drawUI(3, "¿Que deseas hacer? 🤔"))
    print(drawUI(1, ""))
    print(drawUI(3, "A) Quiero jugar ahora mismo 🎮 !"))
    print(drawUI(3, "B) Volver al dashboard principal 😮"))
    print(drawUI(1, ""))
    print("*"*82)
    print()

    opc = input("|| => 😆 Selecciona una opción: ").upper()
    print()

    match opc:
      case "A": 
        id_play = input("|| => 😆 ¿Cúal es el código del juego?: ").upper()
        print()

        # Hacer que el cliente juegue cualquier juego que tenga disponible
        if id_play in client_games:
          game_selected = searchByAttribute("id", id_play, "./data/producto.csv")
          lazyMessage("|| Iniciando el juego en ", 5)
          runFile(game_selected.get("path"))
          print()
          lazyMessage("|| Volviendo a casa en ", 3)
          print()
          return myGames(type_of_user, user_id)
        
        else:
          print("No tienes un juego con ese código especificado 😛 !", end="\n\n")
          lazyMessage("|| Reiniciando en ", 3)
          return myGames(type_of_user, user_id)

      case "B":
        from app.dashboard import userDashboard
        return userDashboard(type_of_user, user_id)
      case _: 
        print("No válido, seleccione una opción nuevamente 🤭 !", end="\n\n")
        lazyMessage("|| Reiniciando en ", 3)
        return myGames(type_of_user, user_id)
    
