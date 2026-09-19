# Passo a passo: criar o "Especialista da minha área" em sala

Este é o roteiro do bloco 3.4. Cada um cria o próprio agente, na própria área.

> Dica: crie o metaprompt no arena.ai antes, de graça, e traga só o resultado para o Claude. Token pago é para executar, não para rascunhar.

## 1. Faça a entrevista no arena.ai

No arena.ai, cole o prompt de entrevista abaixo e responda às cinco perguntas.

```
Papel: Você é o entrevistador que vai escrever a alma do meu agente de I.A.
Tarefa: Faça cinco perguntas, uma de cada vez, e espere cada resposta: minha
área; como me apresento ao cliente; três regras de como escrevo; três coisas
que o agente nunca faz; o tom que eu uso. No fim, gere o arquivo SKILL.md com
name e description (até 200 caracteres) no topo e as seções Identidade, Como
falo, O que só eu faço e O que nunca faço.
Contexto: Sou advogado e vou instalar esse arquivo no Claude como skill.
Regra: Use as minhas palavras. Não invente nada que eu não disse. Se não
tiver certeza de algo, me pergunte antes de fazer.
```

## 2. Leia e corrija o arquivo gerado

Confira se a sua voz está ali: o tom que você descreveu aparece nas regras de escrita? O "O que nunca faço" cobre o que você mais teme que a IA faça errado na sua área? Ajuste o que precisar, direto no arquivo.

## 3. Instale em Customize > Skills

1. Vá em **Customize > Skills**.
2. Clique em **+** e em **Add**.
3. Envie o `SKILL.md` corrigido.
4. Confirme que aparece na lista.

## 4. Teste com uma pergunta real da sua área

Abra uma conversa nova e peça algo típico da sua área, deixando o Claude decidir se usa o agente pela descrição, ou peça direto: "use o especialista da minha área para [TAREFA]".

## 5. Os POPs ficam à parte

Os POPs, regras gerais do escritório, ficam na infraestrutura (bloco 4, pasta `08_INFRAESTRUTURA\POPS\`). Este agente obedece à SOUL própria mais os POPs que se aplicam a ele.

## 6. Se quiser tentar o caminho de subagente (aba Code)

Este caminho está marcado **[CONFIRMAR NO DESKTOP]** no esqueleto. Se quiser testar, na aba Code peça: "crie um subagente em .claude/agents/[nome].md com este conteúdo: [cole os quatro blocos da SOUL]". Depois, invoque pelo nome numa sessão de Code. Se não funcionar, use o caminho de Customize > Skills, que é o confirmado.

## 7. Se a aba Code não achar a skill

**[CONFIRMAR NO DESKTOP]**: não está confirmado se a aba Code enxerga skills instaladas em Customize > Skills. Se a aba Code não encontrar o seu especialista, copie a pasta da skill para `.claude\skills\<nome-da-skill>\SKILL.md`, dentro da pasta do escritório (a aba Code lê skills do projeto ali). Teste de novo depois de copiar.

---

*Passo a passo do kit da imersão de 19/09/2026, bloco 3.4.*
