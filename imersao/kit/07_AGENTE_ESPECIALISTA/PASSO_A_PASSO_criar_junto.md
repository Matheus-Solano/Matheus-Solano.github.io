# Passo a passo: criar o "Especialista da minha área" em sala

Este é o roteiro do bloco 3.4. Cada um cria o próprio agente, na própria área.

> Dica: crie o metaprompt no arena.ai antes, de graça, e traga só o resultado para o Claude. Token pago é para executar, não para rascunhar.

## 1. Faça a entrevista no arena.ai

No arena.ai, cole o prompt de entrevista abaixo e responda às cinco perguntas.

```
Aja como o entrevistador que constrói a SOUL do meu agente jurídico. Me faça,
uma de cada vez, estas cinco perguntas, e espere minha resposta antes da
próxima:

1. Em que área do direito este agente atua, e para qual escritório?
2. Como você se apresenta a este agente (seu nome, cidade/UF, se há mais
   gente no escritório)?
3. Quais são as três regras de como você escreve?
4. Quais são as três coisas que este agente nunca faz?
5. Qual é o tom deste agente (ex: técnico e conservador, ou direto e
   combativo)?

Ao final das cinco respostas, gere um arquivo chamado soul_[area].md, com os
blocos Identidade, Como falo, O que só eu faço e O que nunca faço, sem
travessão, frases curtas.
```

## 2. Leia e corrija o arquivo gerado

Confira se a sua voz está ali: o tom que você descreveu aparece nas regras de escrita? O "O que nunca faço" cobre o que você mais teme que a IA faça errado na sua área? Ajuste o que precisar, direto no arquivo.

## 3. Instale em Customize > Skills

1. Vá em **Customize > Skills**.
2. Clique em **+** e em **Add**.
3. Envie o `soul_[area].md` corrigido.
4. Confirme que aparece na lista.

## 4. Teste com uma pergunta real da sua área

Abra uma conversa nova e peça algo típico da sua área, deixando o Claude decidir se usa o agente pela descrição, ou peça direto: "use o especialista da minha área para [TAREFA]".

## 5. Os POPs ficam à parte

Os POPs, regras gerais do escritório, ficam na infraestrutura (bloco 4, pasta `08_INFRAESTRUTURA\POPS\`). Este agente obedece à SOUL própria mais os POPs que se aplicam a ele.

## 6. Se quiser tentar o caminho de subagente (aba Code)

Este caminho está marcado **[CONFIRMAR NO DESKTOP]** no esqueleto. Se quiser testar, na aba Code peça: "crie um subagente em .claude/agents/[nome].md com este conteúdo: [cole os quatro blocos da SOUL]". Depois, invoque pelo nome numa sessão de Code. Se não funcionar, use o caminho de Customize > Skills, que é o confirmado.

---

*Passo a passo do kit da imersão de 19/09/2026, bloco 3.4.*
