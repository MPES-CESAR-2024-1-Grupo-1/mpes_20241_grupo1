from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

class Professor(Base):
    __tablename__ = 'professor'

    nome: Mapped[str] = mapped_column(String(64))
    numero_de_telefone: Mapped[str] = mapped_column(String(64))
    disciplina: Mapped[str] = mapped_column(String(64))
    serie: Mapped[str] = mapped_column(String(64))

    def __repr__(self):
        return f"Professor(id={self.id!r}, nome={self.nome!r}, numero de telefone={self.numero_de_telefone!r})"


class LogDeSolicitacao(Base):
    __tablename__ = 'log_de_solicitacoes'

    id_professor: Mapped[int] = mapped_column(ForeignKey('professor.id'))
    tema: Mapped[str] = mapped_column(String(256))
    timestamp: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), default=func.now())


