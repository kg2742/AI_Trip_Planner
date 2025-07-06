from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState, END, START   
from langgraph.prebuilt import ToolNode, tools_condition



class GraphBuilder():
    def __init__(self, graph):
        #self.graph = graph
        self.tools = [

        ]
        self.system_prompt = SYSTEM_PROMPT

    def agent_function(self, state: MessagesState):
        """Main agent function that will be called by the graph."""
        user_question = state["messages"]
        input_question = [self.system_prompt] + user_question
        response = self.llm_with_tools.invoke(input_question)
        return

    def build_graph(self):
        graph_builder = StateGraph(MessagesState)
        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools",ToolNode(tools=self.tools))
        graph_builder.add_edge(START, "agent")
        graph_builder.add_conditional_edges("agent", tools_condition)
        graph_builder.add_edge("tools", "agent")
        graph_builder.add_edge("agent", END)
        self.graph = graph_builder.compile()
        return self.graph

    def __call__(self):
        return self.build_graph()



    # def add_node(self, node_id, node_data):
    #     self.graph.add_node(node_id, **node_data)

    # def add_edge(self, source, target, edge_data):
    #     self.graph.add_edge(source, target, **edge_data)

    # def get_graph(self):
    #     return self.graph