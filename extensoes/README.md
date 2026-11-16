# Extensões / melhorias

Cada melhoria vale até 0,5 ponto e precisa estar bem documentada. Atualize o status conforme o andamento e descreva também em [docs/modelo_computacional.md](../docs/modelo_computacional.md) (seção "Extensões").

Status possíveis: `planejada`, `em andamento`, `concluída`, `descartada`.

| Melhoria | Responsável | Status | Justificativa técnica |
|----------|-------------|--------|-----------------------|
| Probabilidade de convencimento (conversão estocástica em vez de limiar fixo) | A definir | planejada | Torna o modelo mais realista; exige gerador aleatório determinístico por célula/geração para manter a equivalência entre versões |
| Resistência (parte da população mais difícil de convencer) | A definir | planejada | Limiar individual por célula; impacto na propagação e na análise de sensibilidade |
| Influenciadores (células com peso maior na vizinhança) | A definir | planejada | Altera a contagem de vizinhos (soma ponderada); testar impacto na velocidade da propagação |
| Bots (espalhadores que nunca ficam inativos) | A definir | planejada | Mantém fontes persistentes; afeta a condição de parada |
| Redução de comunicação com bitmask (2 bits/célula) | A definir | planejada | Reduz o volume de bytes das linhas de halo na versão distribuída; medir o ganho |
| Otimização sem `deepcopy` (duas matrizes alternadas) | A definir | planejada | Elimina a cópia completa a cada geração; medir ganho no sequencial |
| Visualização (heatmap/GIF) | A definir | planejada | Facilita a análise e a apresentação da propagação |
| Estatísticas extras (pico de espalhadores, geração do pico, velocidade de propagação) | A definir | planejada | Enriquece a análise dos resultados |
