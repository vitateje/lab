#CONTROLLER

pessoas = ["vitor","testerman"]

processos = [{"cadastro":"cadastro", "diagnostico":"diagnostico"}]

grupos = [{"cadastro":"cadastro", "diagnostico":"diagnostico"}]

processo = "diagnostico"

solicitação = 3
etapa = "ok"
serviço = "finalizado"


#BPMN

class bpmn():
    def __init__(self, processo, etapa): #constructor
        self.processo = processo
        self.etapa = etapa

    def consulta_processo(self): #getter
        return f'this is one processo: {self.processo}'

    def altera_processo(self, serviço): #method
        if serviço == "finalizado":
            self.etapa = "nova_etapa"

rgpi = bpmn(processo,etapa)

print(rgpi.etapa)
print(rgpi.consulta_processo())
rgpi.altera_processo(serviço)
print(rgpi.etapa)


#RPG

class personagem():
    def __init__(self, nome, força):
        self.nome = "Lucas"
        self.força = força
        

class guerreiro(personagem):
    def __init__(self, nome,força):
        self.nome = nome

vitor = guerreiro("vitor", 15)

print(vitor.nome)
