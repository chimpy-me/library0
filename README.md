# library0

Open-cataloging-protocol tooling — the reference implementation of [LibrarySeedar](https://github.com/chimpy-me) v0 schemas, federation envelopes, and signed Parquet/DuckLake snapshot emission.

**Status:** alpha. Friday-2026-05-08 demo target.

## What it does

`library0` reads a markdown+frontmatter vault, validates each record against a per-record-type JSON Schema, resolves authority cross-references, wraps records in a v0 federation envelope, emits per-type Parquet sidecars + a DuckLake catalog, and signs the catalog with `minisign`.

## License

Apache 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
