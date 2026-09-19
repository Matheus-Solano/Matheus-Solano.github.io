# Nomenclatura do escritório

> Um nome de arquivo bem feito diz, sem abrir o arquivo, o que ele é, de qual caso e de quando.

## Padrão de nome de arquivo

```
[NUMERO]_[TIPO-DO-DOCUMENTO]_[DATA-AAAA-MM-DD].[extensão]
```

- **NUMERO:** dois dígitos, na ordem em que o documento entrou ou foi produzido no caso (01, 02, 03...).
- **TIPO-DO-DOCUMENTO:** em minúsculo, com hífen, sem espaço. Exemplos: `rg-autor`, `comprovante-residencia`, `extracao-forense`, `peticao-inicial`, `peca-final`.
- **DATA:** sempre no formato ano-mês-dia, para ordenar certo por nome.
- **extensão:** `.md` para o que o escritório produz, `.pdf` para documento oficial ou peça protocolada, `.docx` só na peça final antes do protocolo.

## Exemplos

- `01_rg-autor_2026-09-19.pdf`
- `04_pesquisa-jurisprudencia_2026-09-19.md`
- `11_peca-final_2026-09-22.docx`

## Exceção: arquivo padrão gerado por skill

Arquivos padrão que uma skill sempre gera com o mesmo nome ficam fora deste padrão, por exemplo `analises/pesquisa_360.md`, `pecas/inicial_fatos.md`, `resumo.md` e `modelo_peca.md`. A regra `[NUMERO]_[TIPO-DO-DOCUMENTO]_[DATA]` vale para os documentos do caso, originais e versões protocoladas, não para esses arquivos de trabalho de nome fixo.

## Regras

1. Nunca renomeie o arquivo original dentro de `originais/`. O nome padronizado é só para a cópia de trabalho.
2. Nunca dê número de sequência a duplicata ou a versão anterior de um documento já numerado.
3. Nunca numere documento que não pertence a este caso.
4. Se o conteúdo não permitir identificar o tipo do documento com segurança, use `[CONFERIR]` no lugar do tipo, e pergunte ao advogado.

---

*Esqueleto do kit da imersão de 19/09/2026, bloco 4.1. Baseado na ficha 3.3 "Organizar o caos" de 08_METODO\02_MANUAL_[NOME]_v1.0.md.*
