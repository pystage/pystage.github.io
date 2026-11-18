---
title: "Developers"
menu_title: "Developers"
description: "Documentation, contributing guide, translations and credits for PyStage developers."
nav: developers
weight: 20
lead: "PyStage is an open-source project. This page is for people who want to use the library in depth or help develop it. It is only available in English."
---

## Code and documentation

- [README](https://github.com/pystage/pystage#readme): overview, installation and usage.
- [CONTRIBUTING.md](https://github.com/pystage/pystage/blob/development/CONTRIBUTING.md): how to propose changes (GitHub Flow, base branch `development`).
- [TRANSLATING.md](https://github.com/pystage/pystage/blob/development/TRANSLATING.md): how translations work.
- [Read the Docs](https://pystage.readthedocs.io/): the technical reference for the library, the converter and the localisation tools.
- [GitHub](https://github.com/pystage/pystage) for the source and the [issue tracker](https://github.com/pystage/pystage/issues), [PyPI](https://pypi.org/project/pystage/) for the package.
- This website has its own repository, [pystage.github.io](https://github.com/pystage/pystage.github.io).

## Add a language

PyStage is English-canonical at its core; each language is a facade package (for example `pystage.de`) plus a table of dropdown values and messages. The steps are in [TRANSLATING.md](https://github.com/pystage/pystage/blob/development/TRANSLATING.md). For the website, a language needs `i18n/<lang>.toml` and the pages in `content/<lang>/`.

## Maintainer

- Kai Eckert, Mannheim Technical University

## Contributors

- Branden Husted, Calvin University
- Neil Mitchell
- Zhonglin Niu, Calvin University
- Victor Norman, Calvin University
- Florian Rupp
- daolong (ahlongxp)

## License

PyStage is released under the MIT license.
