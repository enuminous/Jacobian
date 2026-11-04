.PHONY: fetch build verify axioms clean
fetch:
	bash scripts/fetch-source.sh
build: verify
verify:
	bash scripts/verify.sh
axioms: verify
clean:
	rm -rf .replay
