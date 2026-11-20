
emails_concelhos = {
    "lisboa":"lisboa@kmail.com",
    "Porto":"porto@kmail.com",
    "Faro":"faro@kmail.com",
}



email = emails_concelhos["Faro"]
print(email)




email = emails_concelhos["Faro"]
print(email)



emails_concelhos["Braga"] = "braga1@kmail.com"
print(emails_concelhos)



print(emails_concelhos.keys())

for concelho in emails_concelhos:
  email = emails_concelhos[concelho]
  print(email)



emails_concelhos.pop('Faro')
print(emails_concelhos)



if "lisboa" in emails_concelhos:
  print("Existe")
else:
  print("Não Existe")



if "lisboa@kmail.com" in emails_concelhos.values():
  print("Existe")
else:
  print("Não Existe")

emails_concelhos["Braga"] = "braga1@kmail.com"
print(emails_concelhos)

"""Quero descobrir nomes dos concelhos"""

print(emails_concelhos.keys())

for concelho in emails_concelhos:
  email = emails_concelhos[concelho]
  print(email)

"""RETIRAR / ELIMINAR"""

emails_concelhos.pop('Faro')
print(emails_concelhos)

"""VERIFICAR SE EXISTE"""

if "lisboa" in emails_concelhos:
  print("Existe")
else:
  print("Não Existe")

"""VERIFICAR SE OS VALORES EXISTEM"""

if "lisboa@kmail.com" in emails_concelhos.values():
  print("Existe")
else:
  print("Não Existe")