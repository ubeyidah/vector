# Vector Changelog

All notable changes to this project will be documented in this file.

## [v0.2.0] - 2025-11-05

### Added

- `feat(memory)`: Add persistent JSON memory to save and load chat history.

### Fixed

- `fix(memory)`: Use the correct `get_history()` method to save chat session.

## [v0.1.0] - 2025-11-02

### Added

- `feat`: Initial project structure with `src/` and `ChatAssistant` class
- `feat`: Add streaming output from the Gemini API
- `feat`: Add chat session (memory) and system prompt
- `ci`: Add Ruff linter workflow (triggered on push/pr to main)
- `docs`: Add `README.md`, `requirements.txt`, `.gitignore`, and `CHANGELOG.md`
