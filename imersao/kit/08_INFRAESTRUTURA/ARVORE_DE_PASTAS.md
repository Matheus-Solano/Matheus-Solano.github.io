# Árvore de pastas do escritório

> A regra é uma só: uma pasta por caso. Tudo o mais é consequência dela.

## Estrutura padrão

```
[NOME DO ESCRITÓRIO]/
  INFRAESTRUTURA.md
  CLAUDE.md
  NOMENCLATURA.md
  BRAND_VOICE.md
  DESIGN_SYSTEM.md
  _modelos/
    [modelos de peça, contrato, proposta do escritório]
  _acervo/
    [ÁREA 1]/
    [ÁREA 2]/
      [teses e jurisprudência que o escritório já validou nesta área]
  [NOME DO CLIENTE 1]/
    [NOME DO CASO 1]/
      originais/
        [cópia intocada de tudo que o cliente enviou]
      CLAUDE.md (ou "memoria.md")
        [o prontuário deste caso: decisões, pendências, prazos, armadilhas]
      01_transcricao_reuniao.md
      02_extracao_forense.md
      03_organizacao_documentos.md
      04_pesquisa_jurisprudencia.md
      05_viabilidade.md
      06_proposta_honorarios.md
      07_contrato.md
      08_estrategia.md
      09_requisitos_formais.md
      10_roteiro_capitulos.md
      11_peca_final.docx
      12_revisao.md
    [NOME DO CASO 2]/
      [mesma estrutura]
  [NOME DO CLIENTE 2]/
    [mesma estrutura]
```

## A regra-mãe: uma pasta por caso

- Cada cliente tem uma pasta própria. Dentro dela, cada caso tem a própria pasta.
- Nunca misture dois casos do mesmo cliente na mesma pasta.
- Nunca trabalhe um caso em conversa solta, sem pasta. "Cada conversa nova sem pasta é uma pasta vazia sem contexto."

## A subpasta `originais`

- Todo documento que o cliente enviar vai primeiro, sem alteração nenhuma, para `originais/`.
- Depois de organizado e renomeado, o documento processado fica na pasta do caso, mas o original nunca é apagado nem sobrescrito.

## O acervo (`_acervo`)

- Fora das pastas de caso, o escritório mantém um acervo por área do direito.
- Ali entram teses que já funcionaram, modelos e pareceres, não o processo inteiro de nenhum cliente.
- Consulte o acervo antes de pesquisar em plataforma aberta.

## Formato dos arquivos

- Prefira `.md` a `.pdf` ou `.docx` para tudo o que o escritório mesmo produz (menor, lido por qualquer sistema).
- O `.docx` fica reservado para a peça final, no padrão do tribunal.

---

*Esqueleto do kit da imersão de 19/09/2026, bloco 4.1. Baseado na ficha 2.a "Uma pasta por caso" de 08_METODO\02_MANUAL_[NOME]_v1.0.md.*
