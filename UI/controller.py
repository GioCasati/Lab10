import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._txtAnno.disabled = True
        self._view._btnCalcola.disabled = True
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
        n, e = self._model._buildGraph(anno)
        self._view._txt_result.controls.append(ft.Text(f"Grafo creato con {n} nodi e {e} archi"))
        self._view._txt_result.controls.append(ft.Text(f"Lista di stati con i confinanti:"))
        for stato, nConfinanti in self._model._getGraphInfos():
            self._view._txt_result.controls.append(ft.Text(f"{stato} - {nConfinanti} confinanti"))
        self._view._txtAnno.disabled = False
        self._view._btnCalcola.disabled = False
        self._view.update_page()