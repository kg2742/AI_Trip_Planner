
import os
from dotenv import load_dotenv
from typing import Literal, Optional, Any
from pydantic import BaseModel, Field
from utils.config_loader import load_config
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI




class ConfigLoader:
    def __init__(self, config_path):
        print(f"Loading config...")
        self.config = load_config()
   
    def __getitem__(self, item):
        return self.config[item]

class ModelLoader(BaseModel):
    model_provider: Literal["openai", "groq"] = "groq"
    config: Optional[ConfigLoader] = Field(default = None, exclude=True)

    def model_post_init(self, __context: Any) -> None:       
        #print(f"Loading config...")
        self.config = ConfigLoader()
    
    class Config:
        arbitrary_types_allowed = True

    def load_llm(self) -> Any:
        """ Load LLM and return the model instance."""

        print("LLM loading...")
        print(f"Model provider: {self.model_provider}")

        if self.model_provider == "groq":
            print("Loading LLM from Groq...")
            groq_api_key = os.getenv("GROQ_API_KEY")
            model_name = self.config['llm']['groq']['model_name']
            llm = ChatGroq(model=model_name, api_key=groq_api_key)
            print(f"Loaded Groq model: {model_name}")
        elif self.model_provider == "openai":
            print("Loading LLM from OpenAI...")
            openai_api_key = os.getenv("OPENAI_API_KEY")
            model_name = self.config['llm']['openai']['model_name']
            llm = ChatOpenAI(model="o4-mini", api_key=openai_api_key)
            print(f"Loaded OpenAI model: {model_name}")
        else:
            raise ValueError(f"Unsupported model provider: {self.model_provider}")

        return llm




        
        

        
        


