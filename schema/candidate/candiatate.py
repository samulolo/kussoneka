from pydantic import (BaseModel,
                     EmailStr, field_validator,
                     ValidationInfo)
import re

EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$"


class CandidateCreate(BaseModel):

    name : str
    email : EmailStr
    
    
    @field_validator('name, email', mode='after')
    @classmethod
    def check_fields(cls, value : str, info : ValidationInfo):

        if not value.strip() or value.strip() == '':
            raise ValueError(f"O campo f{info.field_name} não pode estar vazio")
        return value
    

    @field_validator("email", mode='after')
    @classmethod
    def validate_email(cls, value : str):

        if not re.search(EMAIL_REGEX, value):
            raise ValueError("O email está em um formato incorreto, informe um formato válido")
        return value
