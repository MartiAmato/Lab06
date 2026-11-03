import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
- Rappresenta l'interfaccia utente
- Riceve i dati dal MODELLO e li presenta senza modificarli
'''


class View:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Lab06"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.scroll = ft.ScrollMode.AUTO

        self.alert = AlertManager(page)
        self.controller = None

        self.txt_titolo = None
        self.txt_responsabile = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        self.txt_titolo = ft.Text(value=self.controller.get_nome(), size=38, weight=ft.FontWeight.BOLD)
        self.txt_responsabile = ft.Text(
            value=f"Responsabile: {self.controller.get_responsabile()}",
            size=16,
            weight=ft.FontWeight.BOLD
        )

        self.input_responsabile = ft.TextField(value=self.controller.get_responsabile(), label="Responsabile")

        # ListView con altezza fissa (height=180) per evitare il collasso della pagina
        self.lista_strumenti = ft.ListView(height=180, spacing=5, padding=10, auto_scroll=True)
        self.input_tipo_strumento = ft.TextField(label="Tipo")
        self.lista_strumenti_ricerca = ft.ListView(height=180, spacing=5, padding=10, auto_scroll=True)

        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # Ripristinato ft.Button come nel tuo ambiente
        pulsante_conferma_responsabile = ft.Button("Conferma", on_click=self.controller.conferma_responsabile)

        self.pulsante_mostra = ft.Button(
            "Mostra",  # Passiamo la stringa come primo argomento, senza usare content=""
            on_click=self.controller.mostra_strumenti,
            style=ft.ButtonStyle(shape=ft.StadiumBorder()),
        )

        self.pulsante_cerca = ft.Button(
            "Cerca",  # Passiamo la stringa come primo argomento
            on_click=self.controller.cerca_strumenti,
            style=ft.ButtonStyle(shape=ft.StadiumBorder()),
        )

        # --- LAYOUT ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            self.txt_responsabile,
            ft.Divider(),

            # Sezione 2
            ft.Text("Modifica Informazioni", size=20),
            ft.Row(spacing=200, controls=[self.input_responsabile, pulsante_conferma_responsabile],
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            # Sezione 3
            ft.Row(controls=[ft.Text("Strumenti", size=20), self.pulsante_mostra]),
            self.lista_strumenti,
            ft.Divider(),

            # Sezione 4
            ft.Row(controls=[ft.Text("Cerca strumento per tipo", size=20), self.input_tipo_strumento,
                             self.pulsante_cerca]),
            self.lista_strumenti_ricerca,
            ft.Divider(),
        )

    def cambia_tema(self, e):
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()