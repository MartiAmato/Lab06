import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

# Altre Funzioni Event Handler
    def mostra_strumenti(self, e):
        lista_strumenti = self._model.get_strumenti() #chiedo al model di darmi la lista di tutti gli strumenti
        self._view.lista_strumenti.controls.clear() #pulisco l'output cosi se premo due volte il tasto mostra non fa niente
        if lista_strumenti is not None:
            for strumento in lista_strumenti:
                testo_strumento = ft.Text(str(strumento))
                self._view.lista_strumenti.controls.append(testo_strumento)
        else:
            self._view.lista_strumenti.controls.append(ft.Text("nessuno strumento trovato"))
        self._view.update()

    def cerca_strumenti(self, e):
        self._view.lista_strumenti_ricerca.controls.clear() #pulisco l'output cosi se premo due volte il tasto mostra non fa niente
        tipo_cercato = self._view.input_tipo_strumento.value #vedo cosa ha cercato l'utente
        risultati = self._model.cerca_strumenti_per_tipo(tipo_cercato)
        if risultati:
            for strumento in risultati:
                testo_strumento = ft.Text(str(strumento))
                self._view.lista_strumenti_ricerca.controls.append(testo_strumento)
        else:
            self._view.lista_strumenti_ricerca.controls.append(ft.Text("nessuno strumento trovato"))
        self._view.update()