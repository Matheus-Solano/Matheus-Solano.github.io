# Passo a passo: criar a skill Jurisprudência 360 + Viabilidade em sala

Este é o roteiro do bloco 3.1. Você não abre o SKILL.md pronto agora. Você constrói a sua, do zero, com o Claude, e só depois compara com o gabarito desta pasta.

> Dica: crie o metaprompt no arena.ai antes, de graça, e traga só o resultado para o Claude. Token pago é para executar, não para rascunhar.

## 1. Abra o esqueleto

Abra `03_SKILL_ESQUELETO\SKILL.md` (a mesma pasta acima) e `03_KIT_DRIVE\03_STARTER_PACK\pesquisa-jurisprudencia-360\SKILL.md`, do Starter Pack. O primeiro dá a forma, o segundo dá o conteúdo de pesquisa que você vai herdar.

## 2. Diga ao Claude o ponto controvertido do seu caso

Escolha um ponto controvertido real, do seu próprio caso ou do caso da sala. Uma frase só. Exemplo: "vício do produto configura fato do produto ou fato do serviço, para fins de prazo prescricional".

## 3. Digite este prompt para o Claude gerar o SKILL.md a partir do esqueleto

Copie, ajuste o que estiver entre colchetes e cole no Chat ou no Cowork:

```
Aja como o meu redator de skills. Use o esqueleto em 03_SKILL_ESQUELETO/SKILL.md
como forma e o conteúdo de pesquisa de
03_KIT_DRIVE/03_STARTER_PACK/pesquisa-jurisprudencia-360/SKILL.md como base de
processo de busca. Crie uma skill chamada "jurisprudencia-360-viabilidade" que:

1. recebe um ponto controvertido e pesquisa jurisprudência favorável e contrária,
   em ordem de autoridade dos tribunais (STF, STJ, TST, TJs, TRFs);
2. nunca inventa julgado: todo julgado citado precisa ter sido validado por
   inteiro teor ou fonte oficial, marcado [CONFIRMADO], ou marcado
   [NÃO VERIFICÁVEL] se não deu para confirmar;
3. depois da pesquisa validada, cruza com o caso concreto e devolve uma nota de
   viabilidade de 0 a 10, com 5 critérios próprios (defina quais fazem sentido
   para [SUA ÁREA]), matriz de risco curta e recomendação em uma frase, inclusive
   a possibilidade de recomendar não seguir.

O ponto controvertido deste caso é: [SEU PONTO CONTROVERTIDO].
O tribunal de referência é: [SEU TRIBUNAL].

Escreva o SKILL.md completo, com frontmatter name e description (até 200
caracteres), sem travessão, frases curtas, no formato do esqueleto. Se não
tiver certeza de algo, me pergunte antes de fazer.
```

## 4. Leia o resultado antes de instalar

Confira se o Claude incluiu os marcadores [CONFIRMADO] e [NÃO VERIFICÁVEL], se os 5 critérios de viabilidade fazem sentido para a sua área, e se a recomendação final aparece em uma frase só. Se faltar algo, peça o ajuste, não recomece do zero.

## 5. Instale em Customize > Skills

1. Vá em **Customize > Skills** no Claude Desktop.
2. Clique em **+** e em **Add**.
3. Envie o arquivo `SKILL.md` que o Claude acabou de gerar.
4. Confirme que ela aparece na lista.

## 6. Rode com o ponto controvertido do seu caso

Abra uma conversa nova e peça: "rode a skill jurisprudencia-360-viabilidade para o ponto controvertido [SEU PONTO]". Confira se cada julgado citado veio com o marcador certo.

## Se a aba Code não achar a skill

**[CONFIRMAR NO DESKTOP]**: não está confirmado se a aba Code enxerga skills instaladas em Customize > Skills. Se a aba Code não encontrar a sua skill, copie a pasta dela para `.claude\skills\jurisprudencia-360-viabilidade\SKILL.md`, dentro da pasta do escritório (a aba Code lê skills do projeto ali). Teste de novo depois de copiar.

## Comparando com o gabarito

Depois de rodar a sua, abra o `SKILL.md` desta pasta (a versão completa do kit) e compare. Não existe versão errada: existe a que ficou boa o suficiente para o seu escritório usar segunda-feira.

---

*Passo a passo do kit da imersão de 19/09/2026, bloco 3.1.*
