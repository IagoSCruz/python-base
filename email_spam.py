msg_tmplt = """
Olá, prezado(a) %(name)s, tudo bem?
Informamos que o veículo %(car_model)s está disponível para locação.
Viaje agora mesmo reservando conosco e garanta até %(business_day)d dias para aproveitar por nossa conta!

A diária está no valor de %(cust_freight).2f alugando conosco até o dia 31/10/23!

Para garantir imediatamente, clique no link abaixo.
%(link_car)s

Obrigado pela atenção!
"""

clients = ['Iago Cruz', 'Bruna Medeiros', 'Laura Louzada', 'Linus Torvalds']


for client in clients:
    print(
        msg_tmplt % 
            {
            "name":client,
            "car_model":"Volkswagen UP 2022",
            "business_day": 2,
            "cust_freight": 68,
            "link_car":"https://reserveaquiveiculos.com.br"   
            }
    )