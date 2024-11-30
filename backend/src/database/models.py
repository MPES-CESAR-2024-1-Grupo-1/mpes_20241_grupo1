from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime, Column, Boolean
from sqlalchemy.sql import func
from typing import List

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement="auto", )

class Professor(Base):
    __tablename__ = 'professor'

    nome: Mapped[str] = mapped_column(String(64), nullable=True)
    numero_de_telefone: Mapped[str] = mapped_column(String(64))
    disciplina: Mapped[str] = mapped_column(String(64), nullable=True)
    serie: Mapped[str] = mapped_column(String(64), nullable=True)
    logs_de_solicitacao: Mapped[List["LogDeSolicitacao"]] = relationship(back_populates="professor")
    threads_openai: Mapped[List["ThreadOpenAI"]] = relationship(back_populates="professor")

    def __repr__(self):
        return f"Professor(id={self.id!r}, nome={self.nome!r}, numero de telefone={self.numero_de_telefone!r})"


class LogDeSolicitacao(Base):
    __tablename__ = 'log_de_solicitacoes'

    id_professor: Mapped[int] = mapped_column(ForeignKey('professor.id'))
    tema: Mapped[str] = mapped_column(String(256))
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    professor: Mapped["Professor"] = relationship(back_populates="logs_de_solicitacao")


class ThreadOpenAI(Base):
    __tablename__ = 'thread_openai'

    id_professor: Mapped[int] = mapped_column(ForeignKey('professor.id'))
    id_openai: Mapped[str] = mapped_column(String(128))
    tema: Mapped[str] = mapped_column(String(128), nullable=True)
    tipo: Mapped[str] = mapped_column(String(128), nullable=True)
    finalizada: Mapped[bool] = mapped_column(Boolean(), default=False)
    timestamp_criacao = Column(DateTime(timezone=True), server_default=func.now())
    timestamp_ultima_interacao = Column(DateTime(timezone=True), server_default=func.now())
    professor: Mapped["Professor"] = relationship(back_populates="threads_openai")

    def __repr__(self):
        return f"ThreadOpenAI(id={self.id!r}, id_openai={self.id_openai!r}, id_professor={self.id_professor!r}, tema={self.tema!r}, tipo={self.tipo!r})"


