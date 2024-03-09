from fastapi import APIRouter,  status, HTTPException
from pydantic import BaseModel as BM

router = APIRouter(prefix= "/flashcard")


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel as BM2, Field
from langchain.prompts.prompt import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import List
from config import GOOGLE_API_KEY

class flashcards(BM2):
    question: List[str]
    answer: List[str]

parser = JsonOutputParser(pydantic_object= flashcards)

json_promt = PromptTemplate(
    template = "Using the text provided below generate {number} objective questions and their answers\n{format_instructions}\n{text}\n",
    input_variables=["number",'text'],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

model = ChatGoogleGenerativeAI(model="gemini-pro",
                             temperature=0.1, google_api_key=GOOGLE_API_KEY)

chain = json_promt | model | parser

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

class generate(BM):
    text: str
    number: int

@router.post("/generate")
def get_response(req: generate):

    response = chain.invoke({"number": str(req.number), "text": req.text})

    if not response:
        raise HTTPException(status_code= status.HTTP_503_SERVICE_UNAVAILABLE,
                            detail= "No response obtained from Gemini")
    
    return response
