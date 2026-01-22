# MCP Web Automation Framework

Ez a projekt egy **MCP-alapú (Model Context Protocol)** automatizációs framework, amelynek célja,
hogy egy AI-ügynök **stateful módon** tudjon webböngészőt vezérelni (Playwright segítségével),
konfigurációkból dolgozni, és több lépéses műveleteket összekötni.

A projekt **nem tesztframework**, hanem egy **AI-vezérelt automation platform** alapja.

---

## 🎯 Fő célok

- MCP toolokkal vezérelt automatizáció
- Állapottartó (stateful) böngészőkezelés
- Újrahasználható, kis felelősségű toolok
- AI-barát orchestration (nem újraindít mindent)
- Konfig-vezérelt működés (YAML)

---

## 🧠 Architektúra – alapelvek

- **Tool**: MIT szeretnénk csinálni (AI API)
- **Capability**: HOGYAN történik a művelet
- **State**: Futásidejű állapot (browser, page, stb.)
- **Config reader**: Strukturált adatok kiolvasása
- **Core**: Infrastruktúra (logger, yaml loader)

> A tool **nem kezel state-et**, csak parancsot ad.  
> A state **nem tud MCP-ről**.  
> A capability az egyetlen kapu a state felé.

---

## 📁 Könyvtárstruktúra

