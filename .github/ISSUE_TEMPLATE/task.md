name: Task
description: Arbetsuppgift eller förbättring
title: "[TASK] "
labels: ["task"]
assignees: []
body:
  - type: textarea
    id: goal
    attributes:
      label: Mål / varför
      description: Vad ska uppnås och varför?
    validations:
      required: true
  - type: textarea
    id: dod
    attributes:
      label: Definition of Done
      description: Mätbara kriterier för att anse uppgiften klar.
  - type: checkboxes
    id: checklist
    attributes:
      label: Checklista
      options:
        - label: Kod ändrad
        - label: Tester uppdaterade
        - label: CI grönt
