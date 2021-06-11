"Observer Design Pattern Concept"

from data_model import DataModel
from data_controller import DataController
from pie_graph_view import PieGraphView
from bar_graph_view import BarGraphView
from table_view import TableView


DATA_MODEL = DataModel()


PIE_GRAPH_VIEW = PieGraphView(DATA_MODEL)
BAR_GRAPH_VIEW = BarGraphView(DATA_MODEL)
TABLE_VIEW = TableView(DATA_MODEL)


DATA_CONTROLLER = DataController()


DATA_CONTROLLER.notify([1, 2, 3])


BAR_GRAPH_VIEW.delete()

DATA_CONTROLLER.notify([4, 5, 6])