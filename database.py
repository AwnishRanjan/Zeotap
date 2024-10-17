from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pickle

engine = create_engine('sqlite:///rules.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Rule(Base):
    __tablename__ = 'rules'
    id = Column(Integer, primary_key=True)
    rule_string = Column(String, nullable=False)
    ast_structure = Column(String)  

Base.metadata.create_all(engine)

def save_rule(rule_string, ast_structure):
    serialized_ast = pickle.dumps(ast_structure)
    rule = Rule(rule_string=rule_string, ast_structure=serialized_ast)
    session.add(rule)
    session.commit()

def get_rule(rule_id):
    rule = session.query(Rule).get(rule_id)
    if rule:
        rule.ast_structure = pickle.loads(rule.ast_structure)
        return rule
    return None
