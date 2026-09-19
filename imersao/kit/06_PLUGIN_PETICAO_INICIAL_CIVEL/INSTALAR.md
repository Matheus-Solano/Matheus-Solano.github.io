# Instalar o plugin "Petição inicial cível"

## Skill versus plugin, em 5 linhas

Skill é o POP de uma tarefa: uma habilidade que o Claude usa quando precisa, salva em um único arquivo. Plugin é um pacote maior: reúne uma ou mais skills, comandos e, quando existem, conectores, tudo instalado de uma vez. Se a skill é o profissional com o próprio procedimento, o plugin é o departamento inteiro, pronto. Este plugin tem uma skill (`peticao-inicial-civel`) e um comando (`/peticao`) que a aciona direto. Você não precisa entender a diferença para usar hoje: só precisa saber que o caminho de instalação é diferente.

## Caminho A, instalação como plugin (confirmado para o Desktop)

**[CONFIRMAR NO DESKTOP]** — a verificação técnica (00_VERIFICACAO_DESKTOP.md, item 7) confirma que existe, no Desktop, a rota **+ > Plugins** para navegar, ativar e desinstalar plugins. O que não está confirmado na documentação oficial consultada é o passo exato de "instalar a partir de uma pasta local" por essa UI (ela foi descrita para navegar um marketplace de plugins, não para apontar uma pasta do computador). Teste antes da sala:

1. No Claude Desktop, abra **+ > Plugins**.
2. Procure a opção de adicionar um plugin a partir de uma pasta local ou de um marketplace local.
3. Se existir, aponte para a pasta `06_PLUGIN_PETICAO_INICIAL_CIVEL` (a pasta inteira, com `.claude-plugin`, `skills` e `commands` dentro).
4. Confirme que o comando `/peticao` aparece disponível.

Importante: o comando de terminal `/plugin` para adicionar marketplaces **não existe na aba Code do Desktop** (só no CLI), então esse caminho, se existir, é por UI, não por comando digitado.

## Caminho B, plano B confirmado: copiar a skill para Customize > Skills

Se o Caminho A não funcionar ou não for encontrado na hora, use este, que é o mesmo caminho já confirmado e usado no restante do kit (ver 04_SKILL_DJEN_do_dia):

1. Vá em **Customize > Skills** no Claude Desktop.
2. Clique em **+** e depois em **Add**.
3. Envie o arquivo `skills\peticao-inicial-civel\SKILL.md` desta pasta.
4. Confirme que a skill `peticao-inicial-civel` aparece na lista.
5. Para rodar, não use `/peticao` (esse comando é do plugin). Em vez disso, escreva: "rode a skill peticao-inicial-civel para este caso" ou "monte a petição inicial deste caso, capítulo por capítulo".

O resultado final é o mesmo nos dois caminhos: a petição sai capítulo por capítulo, com gate de aprovação. Muda só o gatilho: `/peticao` no plugin, ou pedir por nome no plano B.

---

*Instruções do kit da imersão de 19/09/2026, bloco 3.3. Base: 00_VERIFICACAO_DESKTOP.md, item 7.*
