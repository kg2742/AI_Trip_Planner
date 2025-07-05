from utils.model_loaders import ModelLoader
from prompt_library.prompt import Prompt
from langgraph.graph import StateGraph, MessageState, END, START
from langgraph.prebuilt import ToolNode, tools_condition



class GraphBuilder():
    def __init__(self, graph):
        #self.graph = graph
        pass

    def agent_function(self):
        pass

    def build_graph(self):
        pass

    def __call__(self):
        pass



    # def add_node(self, node_id, node_data):
    #     self.graph.add_node(node_id, **node_data)

    # def add_edge(self, source, target, edge_data):
    #     self.graph.add_edge(source, target, **edge_data)

    # def get_graph(self):
    #     return self.graph