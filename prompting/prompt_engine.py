# type: ignore
from typing import List, Dict, Any
from prompting.validators import not_empty

def prompt_engine(questions: List, context: Dict = {}) -> Dict:
    payload = {}
    answer = ''
    
    for question in questions:
        
        for key, value in question.items():
            if not context.get(key):
                answer = input(value)
            
            elif context.get(key):
                answer = context.get(key)                
            
            elif '[REQUIRED]' in value:
                not_empty(value=answer)  
            
            elif '[default: ' in value and not answer:
                answer = value.split('[default: ')[1].strip(']')
            
            if isinstance(answer, str):
                if answer.isdigit():
                    answer = int(answer)
                if not answer:
                    continue
    
            payload.update({key: answer})
    
    return payload
    

