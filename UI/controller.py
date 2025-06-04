import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        anno_str = self._view._txtAnno.value
        if not anno_str:
            self._view.create_alert("Inserire un anno!")
            return
        try:
            anno = int(anno_str)
        except ValueError:
            self._view.create_alert("Inserire un anno intero!")
            return
        self._view.create_alert("OK")