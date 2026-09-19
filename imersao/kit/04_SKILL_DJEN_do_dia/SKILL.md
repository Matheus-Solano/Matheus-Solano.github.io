---
name: djen-do-dia
description: "Consulta o DJEN (API pública) pela OAB e UF nos últimos 7 dias, agrupa por processo, resume em duas linhas e sinaliza possível prazo. Use toda manhã ou ao pedir as publicações."
---

# DJEN do dia

Esta skill consulta a API pública do DJEN e devolve uma tabela com as publicações da sua OAB nos últimos 7 dias, já resumidas e sinalizadas.

## Antes de usar, troque os colchetes

- `[NUMERO_OAB]`: o número da sua inscrição na OAB, sem pontos.
- `[UF]`: a sigla do seu estado na OAB, duas letras maiúsculas, por exemplo RJ.

## O que a skill faz, passo a passo

1. Calcule a data de hoje e a data de 7 dias atrás, no formato AAAA-MM-DD.
2. Faça uma requisição GET para:
   `https://comunicaapi.pje.jus.br/api/v1/comunicacao?numeroOab=[NUMERO_OAB]&ufOab=[UF]&dataDisponibilizacaoInicio=[DATA_INICIO]&dataDisponibilizacaoFim=[DATA_FIM]&itensPorPagina=50`
3. Leia o campo `items` da resposta JSON. Cada item tem `siglaTribunal`, `tipoComunicacao`, `nomeOrgao`, `texto` e `data_disponibilizacao`.
4. Se `items` estiver vazio, responda apenas: "Nenhuma publicação para a OAB [NUMERO_OAB]/[UF] nos últimos 7 dias." e pare aqui.
5. Agrupe os itens por processo. Se o item não trouxer número de processo claro, agrupe por `nomeOrgao` mais `data_disponibilizacao`.
6. Para cada publicação, escreva um resumo de no máximo duas linhas, em português, a partir do campo `texto`. Não invente o que o texto não diz.
7. Sinalize "possível prazo" quando o campo `texto` contiver, em qualquer caixa, uma das palavras: "prazo", "intime-se", "manifest" (cobre manifestar, manifestação, manifeste-se).
8. Monte a tabela final, uma linha por publicação:

| Processo / órgão | Tribunal | Tipo | Data | Resumo (2 linhas) | Possível prazo |
|---|---|---|---|---|---|
| ... | [siglaTribunal] | [tipoComunicacao] | [data_disponibilizacao] | [resumo] | Sim / Não |

9. Feche com uma linha: "Isto é um agente que aponta hipótese, não decide cabimento nem conta prazo. Toda publicação marcada 'possível prazo' precisa de conferência e contagem em fonte oficial antes de qualquer decisão."

## Guardrails desta skill

1. Nunca conta prazo nem indica o recurso cabível. Só sinaliza "possível prazo", nunca calcula termo final.
2. Nunca inventa conteúdo de publicação. Se o campo `texto` vier vazio ou cortado, escreva "texto incompleto na fonte, conferir no DJEN".
3. Nunca decide o que fazer com a publicação. Isso é sempre do advogado.

---

*Skill do kit da imersão de 19/09/2026. Baseada no método, itens 2.e "O Chrom e os conectores" e 3.9 "Acompanhamento", e no adendo do DJEN da verificação técnica (00_VERIFICACAO_DESKTOP.md).*
