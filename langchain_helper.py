from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

def genrate_pet_name(animal_type, pet_color):
    # brain 
    llm = OpenAI(temperature=0.7)
    prompt_template_name = PromptTemplate(
        input_variables=["animal_type", "pet_color"],
        template="I have a {animal_type} pet and I want a cool name for it. it is {pet_color} in color.  suggest me five cool names for my pet"
    )
    
    name_chain = LLMChain(llm=llm, prompt=prompt_template_name,output_key="pet_name")
    response = name_chain({'animal_type' : animal_type , 'pet_color' :pet_color })
    return response

if __name__ == "__main__":
    print(genrate_pet_name("tiger", "black"))