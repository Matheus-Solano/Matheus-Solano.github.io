# Passo a passo: instalar e agendar a skill DJEN do dia

## 1. Instalar a skill

1. Abra o Claude Desktop.
2. Vá em **Customize > Skills**.
3. Clique em **+** e depois em **Add** (ou **+ Create skill**, se preferir montar do zero).
4. Envie o arquivo `SKILL.md` desta pasta, já com o seu número de OAB e a sua UF no lugar dos colchetes.
5. Confirme que a skill aparece na lista, com o nome `djen-do-dia`.

## 2. Rodar pela primeira vez

Pode rodar tanto no **Chat** quanto no **Cowork**. Os dois caminhos funcionam.

1. Abra uma conversa nova no Chat (ou no Cowork).
2. Escreva: "rode a skill djen-do-dia".
3. Espere a tabela aparecer. Se vier "nenhuma publicação", também está certo: quer dizer que não houve publicação nos últimos 7 dias.

## 3. Agendar em Code > Routines > Local

1. Vá na aba **Code**, com alguma pasta do escritório aberta.
2. Clique em **Routines**.
3. Clique em **New routine**.
4. Escolha a opção **Local** (não escolha Cloud).
5. Descreva a rotina: "toda manhã às [HORÁRIO], rode a skill djen-do-dia e salve o resultado num arquivo na pasta do escritório".
6. Defina o horário.
7. Salve.

## 4. A regra da rotina local, para não esquecer

A rotina **Local** só dispara com o **Claude Desktop aberto** e o **computador ligado e acordado** no horário marcado. Se o notebook estiver fechado ou desligado, a rotina simplesmente não roda naquele dia. Não é um bug: é como a rotina Local funciona.

Se você precisar que a rotina rode mesmo com o computador desligado, isso hoje só existe na nuvem (Cowork scheduled task ou Routine Cloud), e para o DJEN especificamente isso é a nota abaixo.

## 5. Nota honesta sobre o caminho em nuvem

O teste feito da máquina do titular, em Volta Redonda, mostrou que a API do DJEN responde HTTP 200 com publicações reais quando a consulta parte de dentro do Brasil. A mesma consulta feita de fora do Brasil devolveu 403 (bloqueio geográfico).

As rotinas em nuvem do Claude (Cowork scheduled task e Routine Cloud) rodam em servidores que provavelmente ficam fora do Brasil. Por isso, é provável que uma rotina em nuvem apontada para o DJEN receba 403 e não funcione.

**Conclusão:** hoje, o caminho garantido é a rotina **Local**, no seu próprio computador. O caminho em nuvem fica como "a testar", nunca como promessa. Se quiser tentar mesmo assim, tudo bem, mas saiba que pode não funcionar, e o motivo não é erro seu.

---

*Passo a passo do kit da imersão de 19/09/2026. Baseado em 00_VERIFICACAO_DESKTOP.md, itens 4, 7, 8, 9 e o adendo do DJEN.*
