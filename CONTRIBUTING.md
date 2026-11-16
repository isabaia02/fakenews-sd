# Guia de contribuição

Fluxo de trabalho do grupo no git.

## Regras

1. **`main` é protegida**: ninguém faz commit direto nela. Toda mudança entra por Pull Request.
2. **Branches** no formato `feat/<área>-<descrição>`, por exemplo:
   - `feat/nucleo-calcular-faixa`
   - `feat/paralelo-barreira-threads`
   - `feat/distribuido-protocolo`
   - `feat/bench-grafico-speedup`
   - Para correções: `fix/<área>-<descrição>`; para documentação: `docs/<descrição>`.
3. **Pull Requests** precisam de **1 revisor** (alguém diferente do autor) antes do merge.
4. **Mensagens de commit claras**, no imperativo e em português, com prefixo:
   `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`.
   Exemplo: `feat: implementa troca de linhas de fronteira no trabalhador`.
5. **Todos devem entender o código que commitam.** Se não consegue explicar uma linha na apresentação, não faça commit dela. Quem revisa também precisa entender o que está aprovando.

## Passo a passo

```bash
git checkout main
git pull
git checkout -b feat/<área>-<descrição>
# ... trabalhe, faça commits pequenos ...
git push -u origin feat/<área>-<descrição>
# abra o Pull Request no GitHub e peça revisão
```

## Convenções de código

- Código, comentários e docstrings em **português**; nomes no estilo do projeto (`IGNORANTE`, `criar_grade`, `proxima_geracao`).
- Versões avaliadas: **somente biblioteca padrão** (nada de NumPy, Pandas, Numba, Cython, GPU).
- Não editar `referencia/FakeNews_professor.py`.
- Reutilizar `modelo.calcular_faixa` em todas as versões.
- Rodar os testes antes de abrir o PR: `python -m unittest discover tests`.
