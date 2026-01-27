# Instruções de Commit

Guia rápido para criar mensagens de commit consistentes com o estilo do projeto.


## Tipos (quando usar)

- **feat**: nova funcionalidade
  - Ex: `feat: implement user authentication`
- **fix**: correção de bug
  - Ex: `fix: resolve issue with incorrect date display`
- **docs**: apenas documentação
  - Ex: `docs: update API endpoint descriptions`
- **style**: formatação / espaços / sem mudança de comportamento
  - Ex: `style: apply consistent code formatting`
- **refactor**: refatoração sem mudança de comportamento externo
  - Ex: `refactor: extract database connection logic`
- **perf**: melhorias de performance
  - Ex: `perf: optimize image loading speed`
- **test**: adicionar/ajustar testes
  - Ex: `test: add unit tests for user service`
- **build**: mudanças no build / dependências
  - Ex: `build: update webpack configuration`
- **ci**: alterações em CI/CD
  - Ex: `ci: configure GitHub Actions for automated testing`
- **chore**: tarefas de manutenção / configuração (não altera funcionalidade)
  - Ex: `chore: update dependencies` (uso recomendado para `.gitignore`)
- **revert**: reverter um commit anterior
  - Ex: `revert: feat: implement user authentication (breaks login)`

## Boas práticas

- Seja conciso na descrição (aprox. 50 caracteres).
- Use `scope` quando fizer sentido (ex: `ocr`, `api`, `deps`).
- Explique o *porquê* no corpo do commit, se necessário.
- Para breaking changes, inclua `BREAKING CHANGE:` no corpo e instruções de migração.
- Use verbo no imperativo: `add`, `fix`, `update`.
- Prefira commits pequenos e focados.
- Revise mensagens para clareza e consistência antes de commitar.

### Seguindo essas diretrizes, manteremos um histórico de commits claro e útil para todos os colaboradores do projeto.
