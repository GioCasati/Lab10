import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._statoPartenza = None

    def _readDD(self, e):
        self._statoPartenza = e.control.data

    def handleCalcola(self, e):
        self._statoPartenza = None
        self._view._txtAnno.disabled = True
        self._view._btnCalcola.disabled = True
        self._view._ddStatoPartenza.disabled = True
        self._view._ddStatoPartenza.options.clear()
        self._view._btnRicerca.disabled = True
        self._view._txt_result.controls.clear()
        self._view.update_page()
        anno_str = self._view._txtAnno.value
        if not anno_str:
            self._view.create_alert("Inserire un anno!")
            return
        try:
            anno = int(anno_str)
            if not 1816 <= anno <= 2016:
                self._view.create_alert("Inserire un anno tra 2016 e 1816!")
                return
        except ValueError:
            self._view.create_alert("Inserire un anno intero!")
            return
        n, e, ncc = self._model._buildGraph(anno)
        self._view._txt_result.controls.append(ft.Text(f"Grafo creato correttamente con {n} nodi e {e} archi",
                                                       color='green'))
        self._view._txt_result.controls.append(ft.Text(f"Ci sono {ncc} componenti connesse"))
        self._view._txt_result.controls.append(ft.Text(f"Lista di stati con i confinanti:"))
        for stato, nConfinanti in self._model._getGraphInfos():
            self._view._txt_result.controls.append(ft.Text(f"{stato} - {nConfinanti} confinanti"))
            self._view._ddStatoPartenza.options.append(ft.dropdown.Option(key=str(stato), data=stato, on_click=self._readDD))
        self._view._txtAnno.disabled = False
        self._view._btnCalcola.disabled = False
        self._view._ddStatoPartenza.disabled = False
        self._view._btnRicerca.disabled = False
        self._view.update_page()

    def handleRicerca(self, e):
        self._view._txt_result.controls.clear()
        if not self._statoPartenza:
            self._view.create_alert("Scegliere uno stato")
            self._view.update_page()
            return
        self._view._txt_result.controls.append(ft.Text(f"Partendo da {self._statoPartenza}:"))
        for node in self._model._getConnectedComponentNode(self._statoPartenza):
            self._view._txt_result.controls.append(ft.Text(f"{node} è raggiungibile"))
        self._view.update_page()