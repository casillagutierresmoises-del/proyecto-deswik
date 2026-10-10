"""Rebuild the original evidence archive from checked parts using Python 3."""
from pathlib import Path
import hashlib, json, zipfile

root = Path(__file__).resolve().parent
manifest = json.loads((root / "Partes_SHA256.json").read_text(encoding="utf-8"))
output = (root / manifest["original_filename"]).resolve()
assert output.parent == root.parent, "Output must stay inside the evidence directory"
def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()
for part in manifest["parts"]:
    path = (root / part["filename"]).resolve()
    assert path.parent == root
    assert path.stat().st_size == part["bytes"] and digest(path) == part["sha256"]
if output.exists():
    assert digest(output) == manifest["original_sha256"], "An existing different file will not be replaced"
else:
    with output.open("xb") as target:
        for part in manifest["parts"]:
            with (root / part["filename"]).open("rb") as source:
                for block in iter(lambda: source.read(1024 * 1024), b""):
                    target.write(block)
assert output.stat().st_size == manifest["original_bytes"]
assert digest(output) == manifest["original_sha256"]
with zipfile.ZipFile(output) as archive:
    assert archive.testzip() is None
print("Verified original archive:", output)
