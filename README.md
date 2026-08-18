# Computação Gráfica com Matrizes

Projeto de **Computação Gráfica 2D/3D** e **Processamento de Imagem** construído **estritamente** sobre estruturas próprias de Matrizes e Vetores.

Este repositório serve como ponte entre a matemática abstrata e a engenharia de software aplicada, demonstrando como as mesmas matrizes estudadas teoricamente são usadas para:
- Transformar objetos no plano e no espaço (translação, rotação, escala, shear)
- Compor transformações
- Projectar pontos 3D para 2D
- Aplicar filtros de convolução em imagens

## Objetivos
- Reutilizar e consolidar os conceitos de matrizes e vetores
- Implementar o pipeline básico de transformações geométricas
- Mostrar a aplicação prática da multiplicação de matrizes em gráficos
- Implementar filtros de imagem usando convolução matricial
- Demonstrar a transição clara da teoria para a prática

## Relação com outros repositórios
Este projeto complementa diretamente:
- `algebra-linear-toolset`
- `espacos-vetoriais-dimensao-finita`

## Estrutura

| Pasta              | Conteúdo                                      |
|--------------------|-----------------------------------------------|
| `src/`             | Implementações core (Matrix, Vector, Transforms, Filters) |
| `examples/`        | Exemplos visuais e demonstrações              |
| `docs/`            | Explicações teóricas e do pipeline gráfico    |
| `tests/`           | Testes unitários                              |

## Instalação

```bash
git clone https://github.com/TEU_USER/computacao-grafica-matrizes.git
cd computacao-grafica-matrizes
pip install -r requirements.txt
