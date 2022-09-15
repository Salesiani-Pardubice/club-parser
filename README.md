# Club Parser

Jednoduchý skript sloužící k rozdělení děcek do kroužků dle vyplněných přihlášek.

## Navod

- měj nainstalovanou knihovnu `openpyxl`
  - pro instalaci použij příkaz
  ```
  pip install openpyxl
  ```
- pojmenuj vstupní excel jako `input.xlsx`
- kroužku musejí být v sloupečku s názvem `Kroužky` nebo změn if podmínku (na řádku 17)
- do proměnné `using_col` specifikuj jak0 sloupečky chceš překopírovat