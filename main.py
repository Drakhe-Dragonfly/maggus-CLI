#import

system_name_lists_dict = {"dnd 5e" : "DnD5e",
                     "maggus" : "Maggus"}

def main():
  system_not_found = True
  while system_not_found:
    system = input("Quel système voulez-vous utiliser ?").lower() #prend le système que l'utilisateur veut utiliser
    effective_system = system_name_lists_dict[system]
    if effective_system == "DnD5e" : #vérifie
      system_not_found = False
      pass
    elif effective_system == "Maggus" :
      system_not_found = False
      pass
    else:
      print("Système non implémenté ou non reconnu. Voici la liste des systèmes :")
      for key in system_name_lists_dict:
        print(f"- {system_name_lists_dict[key]}")
  print("Bonne journée.")

main()
