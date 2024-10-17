from fastapi import FastAPI, HTTPException
from src.rule_parser import create_rule
from src.rule_evaluator import evaluate_rule
from src.rule_modifier import modify_operator
from database import get_rule, save_rule

app = FastAPI()
@app.post("/create_rule/")
async def create_rule_endpoint(rule_string: str):
    try:
        ast = create_rule(rule_string)
        save_rule(rule_string, ast)  
        return {"message": "Rule created successfully", "AST": str(ast)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/evaluate_rule/")
async def evaluate_rule_endpoint(ast, data: dict):
    try:
        result = evaluate_rule(ast, data)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/modify_rule/")
async def modify_rule_endpoint(rule_id: int, new_operator: str):
    rule = get_rule(rule_id)
    if rule:
        modify_operator(rule.ast_structure, new_operator)
        save_rule(rule.rule_string, rule.ast_structure)
        return {"message": "Rule modified successfully", "AST": str(rule.ast_structure)}
    else:
        raise HTTPException(status_code=404, detail="Rule not found")
