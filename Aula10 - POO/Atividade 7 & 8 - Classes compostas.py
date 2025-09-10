# Crie uma classe Aluno com atributos nome e nota.
# Depois crie uma classe Turma que tenha uma lista de alunos e um método adicionar_aluno(aluno).
# Crie alguns objetos Aluno e adicione-os à turma.
# 8 - Na classe Aluno, implemente o método __str__ para que, ao imprimir um objeto da classe, apareça algo como:"Aluno: Maria - Nota: 9.5". Teste imprimindo os objetos.

class Aluno:
    def __init__(self, nome: str, nota: float) -> None:
        self.nome = nome
        self.nota = nota

    def __str__(self) -> str: # Atividade 8
        return f"Aluno: {self.nome} - Nota: {self.nota:.2f}"

    def __repr__(self) -> str:
        return f"Pessoa(Nome: {self.nome}, Nota: {self.nota} )"

class Turma:
    def __init__(self, alunos: list[Aluno]) -> None:
        self.alunos = alunos

    def __str__(self) -> str:
        return f"Os alunos que fazem parte da turma são: {self.alunos}"

    def adicionar_aluno(self, aluno: Aluno) -> None:
        self.alunos.append(aluno)
    
aluno1 = Aluno("Jardélia", 9)
aluno2 = Aluno("Wellikson", 8.7)
print(aluno1) # Atividade 8
print(aluno2) # Atividade 8
turma_arte = Turma([])
print(f"Turma inicial: {turma_arte}")
turma_arte.adicionar_aluno(aluno1)
turma_arte.adicionar_aluno(aluno2)
print(f"Turma após Matrículas: {turma_arte}")

