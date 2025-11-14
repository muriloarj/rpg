from __future__ import annotations
from .base import Entidade, Atributos


class Personagem(Entidade):
    """
    Classe base única do jogador.
    Esta versão NÃO implementa a lógica principal de combate.
    """

    def __init__(self, nome: str, atrib: Atributos):
        super().__init__(nome, atrib)
        self.nivel = 1
        self.xp = 0

    def calcular_dano_base(self) -> int:
        """
        Deve retornar um inteiro com o dano base do personagem.
        (ex.: usar self._atrib.ataque, aplicar aleatoriedade/crítico/etc.)
        """
        raise NotImplementedError("Implementar cálculo de dano base do Personagem.")

    def habilidade_especial(self, alvo: Entidade | None = None) -> tuple[int, int]:
        """
        Deve retornar uma tupla (dano_especial, custo_mana).
        Este método é sobrescrito pelas subclasses (Guerreiro, Mago).
        """
        # Como este é o método da classe base, ele retorna 0, forçando o polimorfismo nas subclasses.
        print(f"{self.nome} (Classe Base) não possui habilidade especial definida.")
        return 0, 0 
    
    def ganhar_xp(self, xp_ganho: int) -> None:
        """Adiciona XP e verifica se deve subir de nível."""
        self.xp += xp_ganho
        print(f"🎉 {self.nome} ganhou {xp_ganho} XP!")
