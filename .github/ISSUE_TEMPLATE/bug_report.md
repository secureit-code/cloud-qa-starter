name: Bug report
description: Reportera ett fel
title: "[BUG] "
labels: ["bug"]
assignees: []
body:
  - type: textarea
    id: summary
    attributes:
      label: Sammanfattning
      description: Kort beskrivning av felet.
      placeholder: Vad är fel?
    validations:
      required: true
  - type: textarea
    id: steps
    attributes:
      label: Steg för att reproducera
      description: Lista de exakta stegen för att återskapa felet.
      placeholder: |
        1. Gå till...
        2. Klicka...
        3. Ser...
    validations:
      required: true
  - type: input
    id: expected
    attributes:
      label: Förväntat resultat
    validations:
      required: true
  - type: input
    id: actual
    attributes:
      label: Faktiskt resultat
    validations:
      required: true
  - type: input
    id: env
    attributes:
      label: Miljö
      placeholder: Browser/OS/Version
  - type: textarea
    id: evidence
    attributes:
      label: Skärmbilder/loggar (valfritt)
