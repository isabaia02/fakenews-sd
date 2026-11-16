# Modelo computacional

## Grade

Matriz 2D `linhas x colunas`; cada célula representa uma pessoa. A grade **não é toroidal**: as bordas têm menos vizinhos.

## Estados

| Valor | Constante    | Significado                                   |
|-------|--------------|-----------------------------------------------|
| 0     | `IGNORANTE`  | Ainda não recebeu/acredita na informação      |
| 1     | `ESPALHADOR` | Acredita e compartilha a informação           |
| 2     | `INATIVO`    | Recebeu a informação, mas não compartilha mais |

## Vizinhança de Moore

As 8 células ao redor da célula central:

```
A B C
D X E     vizinhos de X: A B C D E F G H
F G H
```

Cantos têm 3 vizinhos; bordas, 5; células internas, 8.

## Regra de transição

Gerações discretas; a próxima geração é calculada **lendo só da grade atual** (sem atualização "ao vivo"):

- `IGNORANTE` → `ESPALHADOR` se tiver pelo menos `limiar_convencimento` vizinhos `ESPALHADOR`; senão permanece.
- `ESPALHADOR` → `INATIVO` na geração seguinte.
- `INATIVO` → permanece `INATIVO`.

## Condição de parada

A simulação termina quando:

1. não há mais espalhadores (contagem de `ESPALHADOR` = 0 após uma geração), ou
2. o número máximo de gerações é atingido.

## Estado inicial e reprodutibilidade

Grade toda `IGNORANTE`, com `int(linhas * colunas * percentual_espalhadores)` sorteios de posição marcadas como `ESPALHADOR` (posições podem repetir, então o total real pode ser menor). A semente fixa garante reprodutibilidade, requisito para comparar as versões.

## Equivalência entre versões

Com a mesma semente e parâmetros, as versões paralela e distribuída devem produzir as **mesmas contagens por geração** da sequencial. Garantia: todas reutilizam `modelo.calcular_faixa`.

## Extensões

_A preencher: descrever cada melhoria implementada (regra alterada, parâmetros novos, impacto na equivalência com a versão base, como ativar). Ver [extensoes/README.md](../extensoes/README.md)._
