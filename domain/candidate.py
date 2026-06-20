from sqlmodel import SQLModel, Field, Relationship
import uuid


class Candidate(SQLModel, table=True):

    __tablename__ = 'candidates'

    id : uuid.UUID = Field(default_factory=uuid.uuid5, primary_key=True)
    name : str = Field()
    email : str = Field(nullable=False, unique=True)

    professiona_profile : 'CandidateProfile' = Relationship(back_populates='candidate', 
                                                            sa_relationship_kwargs={
                                            "cascade": "all, delete-orphan",
                                            "passive_deletes": True})
