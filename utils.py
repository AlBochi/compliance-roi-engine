import json
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import JSONLoader

class AuditResponseGenerator:
    def __init__(self, api_key):
        self.llm = OpenAI(openai_api_key=api_key, temperature=0.3)
        self.policy_db = "policy_database.json"
        
    def load_policies(self):
        loader = JSONLoader(file_path=self.policy_db, jq_schema='.policies[]')
        return loader.load()
    
    def generate_response(self, question):
        docs = self.load_policies()
        qa_chain = RetrievalQA.from_chain_type(self.llm, chain_type="stuff")
        return qa_chain.run(question + " Answer professionally citing relevant controls.")
