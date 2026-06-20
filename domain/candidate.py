from sqlmodel import SQLModel, Field, Relationship
import uuid
from typing import Optional



class Candidate(SQLModel, table=True):

    __tablename__ = 'candidates'

    id : uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name : str = Field(nullable=False)
    email : str = Field(nullable=False, unique=True, index=True)

    professiona_profile : Optional['CandidateProfile'] = Relationship(back_populates='candidate', 
                                                            sa_relationship_kwargs={
                                            "cascade": "all, delete-orphan",
                                            "passive_deletes": True})
    

    


    # Regra de aplicação de vagas por profivincia 